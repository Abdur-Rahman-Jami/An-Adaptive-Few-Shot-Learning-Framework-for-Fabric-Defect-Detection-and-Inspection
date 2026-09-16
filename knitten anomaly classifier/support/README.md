# Knitted Proto Support Set

Place support images in class-wise subfolders.

Example:

support/
  hole/
    img1.jpg
    img2.jpg
  stain/
    img1.jpg
    img2.jpg
  normal/
    img1.jpg

The pipeline computes one prototype per subfolder using the knitted prototypical backbone and predicts the nearest class for knitted fabric queries.
