# How-I-create-my-identity

## The introduction
Through the exploration of the artist’s identity, the installation “How-I-create-my-identity” investigates the structure of one’s identity, particularly through the lens of time and space.  Time is symbolically represented by the three visual elements of the installation. The two videos “PAST” and “FUTURE” respectively depict the past (in a diapositive style video) and the future (as projected videos and images). In contrast, the triptych “IDENTITY” composed of motionless programmatic pictures represents the illusion of present. These three visual elements explore the deterministic influence of the past on one’s identity, but also how individuals alter their identity in the future. The music “ULTRASYNCHRONICITY” further expands on the link between the past, the illusion of present, and the future.

This deterministic perspective is paradoxically challenged by the theme of the “existential coincidence”. The artist takes the example of his parents’ meeting, conditional on his mother’s family immigrating from Italy to Switzerland in the 1960s. This narrative challenges our interpretation of fortuity: by bridging the past and the future through shared themes and aesthetics, it illustrates the only conceivable present capable of connecting the two, emphasising the deterministic vision behind this artwork. Moreover, the choice of images expands on how space has affected and affects the artist’s identity through cultural and social influences. 

Through the deconstruction of past influences, and the reconstruction of a synthetic future identity, the installation “How-I-create-my-identity” invites the viewer to reflect on the formation of their own identity. The videos and images are presented under the license Open Data Commons Open Database License (ODbL), and all the code used to generate the installation is freely available on GitHub (https://github.com/Mass23/How-I-create-my-identity).

## How to run the code
Run the code from the github repo directory, having loaded the conda environment beforehand.
Create a "data/" directory containing the images you want to use, feel free to use the code I created but do not forget YOU create YOUR identity ;)

- IDENTITY.py: code to create the images triptych using three openstreetmap screenshots.
- PAST.py: code that creates the PAST video, using a mix of openstreetmap screenshots (inside the data/journey/ directory), and photos (inside the data/journey_photos/ directory).
- Spacetime.py: code to create the spacetime plot images, and turn them into a video. (part of the FUTURE video)
- Vesuvius.py: code to blur the videos inside the data/vesuvius/ directory. (part of the FUTURE video)
- Feel free to create a video with these output with your favourite video editor :)
