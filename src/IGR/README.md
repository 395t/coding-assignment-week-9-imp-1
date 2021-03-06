# IGR: Implicit Geometric Regualrization for Learning Shapes

Reconstructing Surfaces
-

IGR introduces a simple loss function to be able to recreate surfaces
given point cloud data.

I ran a set of ablation tests and compared results across datasets

## Long Test: Shows reconstruction loss through 25,000 epochs
    


![LongTest](./visuals/long_test_gif.gif)

![LongTestPlot](./visuals/IGR_LongTest.png)

## Loss Ablations 5k Epochs

- Normal Baseline
- No Eikonal Norm
- Emphasized Eikonal Norm
- No Normal 

![Loss Ablation Plot](./visuals/IGR_Loss_Ablations.png)

![No normals](./visuals/no_norm_animation.gif)
![No Eikonal](./visuals/no_eikonal_animated.gif)

## Optimizer Tests 5k Epochs

- Adam (original)
- AdamW 
- AdaDelta 

![Optimzer Plots](./visuals/IGR_Optimizers_Test.png)

## Dataset Comparisons 5k Epochs

- DFaust 
- ShapeNetCore V2
- ModelNet 10

![Dataset Comparison Plot](./visuals/IGR_Dataset_Comparison.png)

![ShapeNet 0 Animated](./visuals/shapenet0_animated.gif)

![ModelNet 0 Animated](./visuals/modelnet0_animated.gif)

## Point Cloud Sampling Test 5k Epochs

Sampling points per batch at 
- 250 per batch
- 500 per batch
- 1000 per batch
- 2048 (all) per batch

![Point Cloud Sampling](./visuals/IGR_SN_Point_Sampling.png)


# Take Aways

- Normals are extremely helpful for complex shapes
- IGR is bad at finding holes
- Eikonal norm will help train slightly faster (finer details)
- All points are useful for single shape reconstruction
- Adaptive Learning Rate optimizers are not helpful
- Finer details appear after long epochs with diminishing returns


# Table of Results

| Experiment  | Epochs | Loss | Created Reasonable Mesh |
| ------------- | ------------- | ------------- | ------------- |
| Long Test  | 25,000  | 0.05 | yes |
| Baseline  | 5,000  | .066 | yes |
| No Eikonal  | 5,000  | 0.065 | yes |
| Eikonal @ 0.5  | 5,000  | 0.068 | yes |
| No Norms  | 5,000  | 0.002 | No |
| AdamW  | 5,000  | 0.07 | yes |
| AdaDelta  | 5,000  | 0.25 | yes |
| ShapeNet Phone  | 5,000  | .01 | yes |
| ModelNet Table  | 5,000  | 0.003 | yes* (filled in holes) |
| ShapeNet Speaker @ 250pts  | 5,000  | 0.019 | yes |
| ShapeNet Speaker @ 500pts  | 5,000  | 0.008 | yes |
| ShapeNet Speaker @ 1000pts  | 5,000  | 0.006 | yes |
| ShapeNet Speaker @ 1500pts  | 5,000  | 0.008 | yes |
| ShapeNet Speaker @ 2048pts (all)  | 5,000  | 0.007 | yes |


