# How-to-create-your-identity

## 0. Introduction

#### 0.0 General introduction: deconstructing identity
- How does cultural, environmental and hereditary influences shape our identity?
- How can one shape its own identity?

This installation
Open access: DIY
The visual identity of the installation...

 The three locations depicted represent important geographic places that contributed to shape the artist’s identity. The first image on the left depicts an aerial view of Neuchâtel (Switzerland), his hometown. The second one, Lausanne (Switzerland), is the town he currently lives in. And the third one on the right is Naples (Italy) where his mother’s family comes from. By dissecting the construction of his own Identity, the artist also denotes that any identity represents an arbitrary construct. In this sense, this artwork also questions the link between maps and the physical reality. It invites us to reflect on the difference between representation and identity, the model and the referent. “A map is not the territory it represents, but, if correct, it has similar structures to the territory” (1931, Korzybski).

#### 0.1 License
https://creativecommons.org/

## 1. Installation

## 2. Database creation

#### 2.0 OpenStreetMap images

#### 2.1 Cultural heritage photographs

#### 2.2 Visual identity 

## 3. Creation

#### 3.1 Run the code

## 4. Output

#### 4.0 The identity/ folder


## 5. Technical description

#### 5.0 X

#### 5.1 XX
Triptych of images created using python’s matplotlib plotting library. Starting images were created using screenshots of google maps (maps.google.ch/) near Neuchâtel (Switzerland), Lausanne (Switzerland) and the gulf of Naples (Italy). The PIL python library was used to import, manipulate, and extract the images data. Briefly, images were loaded and reduced to a 400 x 400 pixels size and converted to black and white using the convert(‘L’) function. Subsequently, the pixels row averages values were subtracted to the pixel values to get a value representing the deviation from the row mean. The data was plotted as lines, representing the pixel rows, with the x values on the x axis and deviations from the mean on the y axis. Hence, the final image shows a more twisted result in the pixels where brightness is different than the rows average. The code used to produce these images is available on github: https://github.com/Mass23/fig1a_2022/.

#### 5.2 XXX

#### 5.1 geo-identity
