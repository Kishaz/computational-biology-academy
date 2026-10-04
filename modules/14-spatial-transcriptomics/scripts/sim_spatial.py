#!/usr/bin/env python3
"""Spatial transcriptomics with a KNOWN answer: a tissue with three concentric
zones (core / rim / edge), each its own cell type with its own markers. We run
the standard expression-clustering workflow (ignoring position), then plot the
cells back at their real coordinates to see whether the tissue structure
reappears. Teaching only, not real data.

Outputs:
  spatial.csv   per cell: x, y, true_zone, leiden cluster, one marker value
  (prints: n clusters, cluster-vs-zone crosstab, ARI)
"""
import numpy as np, pandas as pd, scanpy as sc, anndata as ad
from sklearn.metrics import adjusted_rand_score
rng = np.random.default_rng(14)
sc.settings.verbosity = 0

N = 1200
N_GENES = 800
MPT = 40   # markers per type

# positions: uniform over a unit disc
r = np.sqrt(rng.uniform(0, 1, N))
th = rng.uniform(0, 2*np.pi, N)
x, y = r*np.cos(th), r*np.sin(th)

# concentric zones of equal area -> three cell types
# boundaries at r = sqrt(1/3) and sqrt(2/3)
b1, b2 = np.sqrt(1/3), np.sqrt(2/3)
zone = np.where(r < b1, 0, np.where(r < b2, 1, 2))
zname = np.array(["core", "rim", "edge"])[zone]

# expression: background + this zone's markers switched on
base = rng.gamma(0.5, 1.0, N_GENES) + 0.1
marker_idx = {t: list(range(t*MPT, (t+1)*MPT)) for t in range(3)}
size = rng.lognormal(0, 0.3, N)
X = np.zeros((N, N_GENES), dtype=np.int64)
for c in range(N):
    m = base.copy()
    m[marker_idx[zone[c]]] += rng.uniform(15, 25)
    X[c] = rng.poisson(m * size[c])

genes = [f"g{n:04d}" for n in range(1, N_GENES+1)]
adata = ad.AnnData(X=X.astype(np.float32))
adata.var_names = genes
adata.obs["zone"] = pd.Categorical(zname)
print(f"Tissue: {N} cells x {N_GENES} genes, 3 concentric zones")

# --- standard expression-clustering workflow (position NOT used) ---
sc.pp.normalize_total(adata, target_sum=1e4)
sc.pp.log1p(adata)
adata.raw = adata
sc.pp.highly_variable_genes(adata, n_top_genes=150)
a2 = adata[:, adata.var.highly_variable].copy()
sc.pp.scale(a2, max_value=10)
sc.tl.pca(a2, n_comps=20, random_state=0)
sc.pp.neighbors(a2, n_neighbors=15, n_pcs=20, random_state=0)
sc.tl.leiden(a2, resolution=0.5, random_state=0, flavor="igraph", n_iterations=2, directed=False)
leiden = a2.obs["leiden"].values

n_clusters = pd.Series(leiden).nunique()
print(f"\nLeiden found {n_clusters} clusters (from expression alone)")
print("\n=== cluster (rows) vs true zone (cols) ===")
print(pd.crosstab(pd.Series(leiden, name="leiden"), adata.obs["zone"]))
ari = adjusted_rand_score(adata.obs["zone"], leiden)
print(f"\nAdjusted Rand Index (clusters vs zones): {ari:.3f}")

rep_marker = genes[marker_idx[0][0]]   # a core marker
out = pd.DataFrame({
    "x": x, "y": y, "true_zone": zname, "leiden": leiden,
    "coreMarker": np.asarray(adata.raw[:, rep_marker].X).ravel(),
})
out.to_csv("spatial.csv", index=False)
print("\nWrote spatial.csv  (core marker:", rep_marker, ")")
