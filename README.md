# Implicit functions - Week 9 Group 1
Papers covered in our repo:
* 	DeepSDF: Learning Continuous Signed Distance Functions for Shape Representation, Park, Florence, Straub, Newcombe, Lovegrove; 2019
* 	Occupancy Networks: Learning 3D Reconstruction in Function Space, Mescheder, Oechsle, Niemeyer, Nowozin, Geiger; 2018
* 	Implicit Geometric Regularization for Learning Shapes, Gropp, Yariv, Haim, Atzmon, Lipman; 2020
* 	Fourier Features Let Networks Learn High Frequency Functions in Low Dimensional Domains, Tancik, Srinivasan, Mildenhall, Fridovich-Keil, Raghavan, Singhal, Ramamoorthi, Barron, Ng; 2020
* 	Implicit Neural Representations with Periodic Activation Functions, Sitzmann, Martel, Bergman, Lindell, Wetzstein; 2020

### Datasets
Each paper had different datasets processed specifically for their models. Finding common datasets was challenging. The following datasets were used across the models:
* DFaust
* ShapeNetCore V2
* ModelNet 10
* **TODO: Add other datasets**

### Architectures
Each paper presented different applications and networks, so there is no common backbone network for this project.



## Reference
* DeepSDF repository, by Schmidt, T. (facebookresearch). https://github.com/facebookresearch/DeepSDF
* **TODO: Add other repos**


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



# Fourier Features Let Networks Learn High Frequency Functions in Low Dimensional Domains



# ![Nature1_best](images/Nature1_best.png)![Nature2_best](images/Nature2_best.png)

# ![Text1_best](images/Text1_best.png)![Text2_best](images/Text2_best.png)

![Nature_best_comp](images/Nature_best_comp.png)

![Text_best_comp](images/Text_best_comp.png)

#### Nature picture PSNR

![Nature_PSNR](images/Nature_PSNR.png)

#### Text picture PSNR

![Text_PSNR](images/Text_PSNR.png)

# SIREN: Implicit Neural Activations with Periodic Activation Functions

## Image Reconstruction

SIREN optimizes the implicit function as a form of an equation of their gradients, laplacians, higher order terms etc.

The following example shows the process of SIREN approximating an image with and the gradients, laplacians over time.

![cameraman_0](https://user-images.githubusercontent.com/25853995/137651682-eedace5c-de85-4782-a2c6-d879eae06582.png)
![cameraman_99](https://user-images.githubusercontent.com/25853995/137651690-ac485956-b742-47ec-88ea-65fb6a0e6ee7.png)
![cameraman_198](https://user-images.githubusercontent.com/25853995/137651694-59ff4476-44d8-4c2b-a241-63c482c00889.png)
![cameraman_297](https://user-images.githubusercontent.com/25853995/137651697-403cceed-02cb-47be-bbbc-20032aacab1a.png)
![cameraman_396](https://user-images.githubusercontent.com/25853995/137651702-2ecf3238-0c62-4c86-8f12-2bbfbe3271c6.png)
![cameraman_495](https://user-images.githubusercontent.com/25853995/137651708-2386b38d-90c4-442c-9232-46924694045a.png)

## Poisson Equation

Since SIREN approximates the underlining function wrt. constraints about its differentials at any order, it's easy to solve the Poisson equation by construction.

We construct the constraints by gradients in order to do so assuming the gradients are everything we know.

The following example shows that SIREN resonably reconstructed the original image.

![cameraman_poisson_100](https://user-images.githubusercontent.com/25853995/137652403-044b879b-e718-43f6-9755-090c6418bc60.png)
![cameraman_poisson_200](https://user-images.githubusercontent.com/25853995/137652406-5b6ad18d-fa96-4a29-a21a-d0bfc6a5de1c.png)
![cameraman_poisson_300](https://user-images.githubusercontent.com/25853995/137652408-3c9ec847-d99e-4700-9c97-244550955074.png)
![cameraman_poisson_400](https://user-images.githubusercontent.com/25853995/137652414-ca9ced0c-fd37-4407-a14f-2ea6e39a95ef.png)
![cameraman_poisson_500](https://user-images.githubusercontent.com/25853995/137652420-4be235b4-e629-4d4a-bce0-8db3201cf326.png)

