---
name: geomloss
category: machine-learning
description: geomloss - Geometric loss functions between point clouds, images and volumes.
tags: [geomloss, machine-learning, geometric-loss, point-clouds]
author: oxo-call-community
source_url: "https://github.com/jeanfeydy/geomloss"
---

## Concepts
- **Geometric Loss**: Computes geometric loss functions between datasets.
- **Optimal Transport**: Implements optimal transport distances.
- **Point Cloud Processing**: Processes point cloud data.
- **Sinkhorn Distance**: Computes Sinkhorn distances.
- **Machine Learning**: Integrates with ML pipelines.

## Pitfalls
- **Computational Complexity**: May be computationally intensive.
- **Memory Usage**: Large datasets require significant memory.
- **Parameter Tuning**: Requires careful parameter adjustment.
- **GPU Acceleration**: Benefits from GPU acceleration.
- **Numerical Stability**: May require numerical stabilization.

## Examples
### Compute Sinkhorn distance
**Args:** `python -c "from geomloss import SinkhornLoss; loss = SinkhornLoss(); d = loss(x, y)"`
**Explanation:** Computes Sinkhorn distance between point clouds.

### With GPU
**Args:** `python -c "loss = SinkhornLoss(blur=0.05); d = loss(x.cuda(), y.cuda())"`
**Explanation:** Uses GPU for acceleration.

### Wasserstein distance
**Args:** `python -c "from geomloss import SamplesLoss; loss = SamplesLoss('sinkhorn'); d = loss(x, y)"`
**Explanation:** Computes Wasserstein distance.

### Batch processing
**Args:** `python -c "loss = SamplesLoss(); distances = [loss(x[i], y[i]) for i in range(N)]"`
**Explanation:** Processes multiple batches.

### Visualize loss
**Args:** `python -c "loss.visualize(x, y, 'loss.png')"`
**Explanation:** Visualizes loss landscape.