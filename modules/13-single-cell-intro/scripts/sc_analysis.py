#!/usr/bin/env python3
"""Single-cell RNA-seq with a KNOWN answer: simulate a mixture of three cell
types (each with its own marker genes), then run the standard Scanpy pipeline
and check that unsupervised clustering + UMAP recover the cell types we built.
Teaching only, not real data.

Outputs:
  umap.csv   per-cell: UMAP coords, leiden cluster, true type, 3 marker values
  (and prints a summary: n clusters, cluster-vs-truth crosstab, ARI)
"""
import numpy as np
import pandas as pd
import scanpy as sc
import anndata as ad
from sklearn.metrics import adjusted_rand_score

rng = np.random.default_rng(13)
sc.settings.verbosity = 0

N_TYPES = 3
PER_TYPE = 300
N_CELLS = N_TYPES * PER_TYPE
N_GENES = 800
MARKERS_PER_TYPE = 40

# true cell type per cell
types = np.repeat([f"type{t+1}" for t in range(N_TYPES)], PER_TYPE)

# background mean expression per gene (low, sparse)
base = rng.gamma(shape=0.5, scale=1.0, size=N_GENES) + 0.1

# marker genes: first 120 genes, 40 per type, elevated only in their type
marker_idx = {t: list(range(t * MARKERS_PER_TYPE, (t + 1) * MARKERS_PER_TYPE))
              for t in range(N_TYPES)}

# per-cell library size factor (varies -> normalisation matters)
size = rng.lognormal(mean=0.0, sigma=0.3, size=N_CELLS)

X = np.zeros((N_CELLS, N_GENES), dtype=np.int64)
for c in range(N_CELLS):
    t = c // PER_TYPE
    mean = base.copy()
    mean[marker_idx[t]] += rng.uniform(15, 25)   # this type's markers switched on
    X[c] = rng.poisson(mean * size[c])

genes = [f"g{n:04d}" for n in range(1, N_GENES + 1)]
adata = ad.AnnData(X=X.astype(np.float32))
adata.var_names = genes
adata.obs_names = [f"cell{i:04d}" for i in range(N_CELLS)]
adata.obs["true_type"] = pd.Categorical(types)

print(f"Starting matrix: {adata.n_obs} cells x {adata.n_vars} genes")

# --- standard Scanpy workflow ---
sc.pp.normalize_total(adata, target_sum=1e4)   # correct for per-cell depth
sc.pp.log1p(adata)
adata.raw = adata
sc.pp.highly_variable_genes(adata, n_top_genes=150)
adata_hvg = adata[:, adata.var.highly_variable].copy()
sc.pp.scale(adata_hvg, max_value=10)
sc.tl.pca(adata_hvg, n_comps=20, random_state=0)
sc.pp.neighbors(adata_hvg, n_neighbors=15, n_pcs=20, random_state=0)
sc.tl.leiden(adata_hvg, resolution=0.5, random_state=0, flavor="igraph", n_iterations=2, directed=False)
sc.tl.umap(adata_hvg, random_state=0)

adata.obs["leiden"] = adata_hvg.obs["leiden"].values
adata.obsm["X_umap"] = adata_hvg.obsm["X_umap"]

n_clusters = adata.obs["leiden"].nunique()
print(f"\nLeiden found {n_clusters} clusters")
ct = pd.crosstab(adata.obs["leiden"], adata.obs["true_type"])
print("\n=== cluster (rows) vs true cell type (cols) ===")
print(ct)
ari = adjusted_rand_score(adata.obs["true_type"], adata.obs["leiden"])
print(f"\nAdjusted Rand Index (clusters vs truth): {ari:.3f}  (1.0 = perfect)")

# one representative marker per type (log-normalised expression), for the figure
rep = {t: genes[marker_idx[t][0]] for t in range(N_TYPES)}
print("representative markers:", rep)
out = pd.DataFrame({
    "umap1": adata.obsm["X_umap"][:, 0],
    "umap2": adata.obsm["X_umap"][:, 1],
    "leiden": adata.obs["leiden"].values,
    "true_type": adata.obs["true_type"].values,
    "markerA": np.asarray(adata.raw[:, rep[0]].X).ravel(),
    "markerB": np.asarray(adata.raw[:, rep[1]].X).ravel(),
    "markerC": np.asarray(adata.raw[:, rep[2]].X).ravel(),
})
out.to_csv("umap.csv", index=False)
print("\nWrote umap.csv")
