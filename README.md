# coding-template

## Summary

The summary can contain but is not limited to:

- Code structure.

- Commands to reproduce your experiments.

- Write-up of your findings and conclusions.

- Ipython notebooks can be organized in `notebooks`.

## Reference

Any code that you borrow or other reference should be properly cited.


# IGR: Implicit Geometric Regualrization for Learning Shapes

[Implementation of IGR can be found here](https://github.com/amosgropp/IGR)

Reconstructing Surfaces
-

IGR introduces a simple loss function to be able to recreate surfaces
given point cloud data.

I ran a set of ablation tests and compared results across datasets

## Long Test: Shows reconstruction loss through 25,000 epochs
    


![LongTest](./src/IGR/visuals/long_test_gif.gif)

![LongTestPlot](./src/IGR/visuals/IGR_LongTest.png)

## Loss Ablations 5k Epochs

- Normal Baseline
- No Eikonal Norm
- Emphasized Eikonal Norm
- No Normal 

![Loss Ablation Plot](./src/IGR/visuals/IGR_Loss_Ablations.png)

![No normals](./src/IGR/visuals/no_norm_animation.gif)
![No Eikonal](./src/IGR/visuals/no_eikonal_animated.gif)

## Optimizer Tests 5k Epochs

- Adam (original)
- AdamW 
- AdaDelta 

![Optimzer Plots](./src/IGR/visuals/IGR_Optimizers_Test.png)

## Dataset Comparisons 5k Epochs

- DFaust 
- ShapeNetCore V2
- ModelNet 10

![Dataset Comparison Plot](./src/IGR/visuals/IGR_Dataset_Comparison.png)

![ShapeNet 0 Animated](./src/IGR/visuals/shapenet0_animated.gif)

![ModelNet 0 Animated](./src/IGR/visuals/modelnet0_animated.gif)

## Point Cloud Sampling Test 5k Epochs

Sampling points per batch at 
- 250 per batch
- 500 per batch
- 1000 per batch
- 2048 (all) per batch

![Point Cloud Sampling](./src/IGR/visuals/IGR_SN_Point_Sampling.png)


## Take Aways For IGR

- Normals are extremely helpful for complex shapes
- IGR is bad at finding holes
- Eikonal norm will help train slightly faster (finer details)
- All points are useful for single shape reconstruction
- Adaptive Learning Rate optimizers are not helpful
- Finer details appear after long epochs with diminishing returns


## Table of Results for IGR

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


# SIREN: Implicit Neural Activations with Periodic Activation Functions

Image Reconstruction
-

SIREN optimizes the implicit function as a form of an equation of their gradients, laplacians, higher order terms etc.

The following example shows the process of SIREN approximating an image with and the gradients, laplacians over time.

![cameraman_0](https://user-images.githubusercontent.com/25853995/137651682-eedace5c-de85-4782-a2c6-d879eae06582.png)
![cameraman_99](https://user-images.githubusercontent.com/25853995/137651690-ac485956-b742-47ec-88ea-65fb6a0e6ee7.png)
![cameraman_198](https://user-images.githubusercontent.com/25853995/137651694-59ff4476-44d8-4c2b-a241-63c482c00889.png)
![cameraman_297](https://user-images.githubusercontent.com/25853995/137651697-403cceed-02cb-47be-bbbc-20032aacab1a.png)
![cameraman_396](https://user-images.githubusercontent.com/25853995/137651702-2ecf3238-0c62-4c86-8f12-2bbfbe3271c6.png)
![cameraman_495](https://user-images.githubusercontent.com/25853995/137651708-2386b38d-90c4-442c-9232-46924694045a.png)
