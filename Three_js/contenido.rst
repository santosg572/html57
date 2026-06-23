Preface vii
Chapter 1: Creating Your First 3D Scene with Three.js 1
Requirements to use Three.js 5
Getting the source code 6
Using Git to clone the repository 7
Downloading and extracting the archive 8
Testing the examples 8
Python-based web servers should work on most Unix/Mac systems 9
Npm-based web server if you've worked with Node.js 9
Portable version Mongoose for Mac and/or Windows 9
Disabling security exceptions in Firefox and Chrome 10
Creating the HTML skeleton 12
Rendering and viewing a 3D object 14
Adding materials, lights, and shadows 19
Expanding your first scene with animations 22
Introducing requestAnimationFrame 22
Animating the cube 24
Bouncing the ball 25
Using dat.GUI to make experimenting easier 26
Automatically resize the output when browser size changes 28
Summary 29
Chapter 2: Basic Components That Make Up a Three.js Scene 31
Creating a scene 31
Basic functionality of a scene 32
Adding fog to the scene 38
Using the overrideMaterial property 40

 of Contents
Chapter 5: Learning to Work with Geometries 129
The basic geometries provided by Three.js 130
Two-dimensional geometries 130
THREE.PlaneGeometry 130
THREE.CircleGeometry 132
THREE.RingGeometry 135
THREE.ShapeGeometry 136
Three-dimensional geometries 142
THREE.BoxGeometry 142
THREE.SphereGeometry 144
THREE.CylinderGeometry 146
THREE.TorusGeometry 148
THREE.TorusKnotGeometry 150
THREE.PolyhedronGeometry 152
Summary 157
Chapter 6: Advanced Geometries and Binary Operations 159
THREE.ConvexGeometry 160
THREE.LatheGeometry 162
Creating a geometry by extruding 163
THREE.ExtrudeGeometry 164
THREE.TubeGeometry 166
Extrude from SVG 168
THREE.ParametricGeometry 171
Creating 3D text 174
Rendering text 174
Adding custom fonts 177
Using binary operations to combine meshes 178
The subtract function 180
The intersect function 184
The union function 186
Summary 187
Chapter 7: Particles, Sprites, and the Point Cloud 189
Understanding particles 190
Particles, THREE.PointCloud, and THREE.PointCloudMaterial 192
Styling particles with the HTML5 canvas 195
Using HTML5 canvas with THREE.CanvasRenderer 195
Using HTML5 canvas with WebGLRenderer 197
Using textures to style particles 201
Working with sprite maps 206
Creating THREE.PointCloud from an advanced geometry 211
Summary 214

ntents
Chapter 8: Creating and Loading Advanced Meshes
and Geometries 215
Geometry grouping and merging 215
Grouping objects together 216
Merging multiple meshes into a single mesh 218
Loading geometries from external resources 220
Saving and loading in Three.js JSON format 222
Saving and loading THREE.Mesh 222
Saving and loading a scene 224
Working with Blender 227
Installing the Three.js exporter in Blender 228
Loading and exporting a model from Blender 230
Importing from 3D file formats 233
The OBJ and MTL formats 233
Loading a Collada model 237
Loading the STL, CTM, VTK, AWD, Assimp, VRML, and Babylon models 238
Show proteins from Protein Data Bank 241
Creating a particle system from a PLY model 244
Summary 245
Chapter 9: Animations and Moving the Camera 247
Basic animations 247
Simple animations 248
Selecting objects 250
Animating with Tween.js 252
Working with the camera 255
TrackballControls 257
FlyControls 259
RollControls 261
FirstPersonControls 262
OrbitControl 264
Morphing and skeletal animation 266
Animation with morph targets 268
Animation with MorphAnimMesh 268
Creating an animation by setting the morphTargetInfluence property 271
Animation using bones and skinning 273
Creating animations using external models 275
Creating a bones animation using Blender 276
Loading an animation from a Collada model 279
Animation loaded from a Quake model 281
Summary 284

f Contents
Chapter 10: Loading and Working with Textures 285
Using textures in materials 285
Loading a texture and applying it to a mesh 286
Using a bump map to create wrinkles 290
Achieving more detailed bumps and wrinkles with a normal map 292
Creating fake shadows using a light map 294
Creating fake reflections using an environment map 296
Specular map 302
Advanced usage of textures 304
Custom UV mapping 304
Repeat wrapping 308
Rendering to canvas and using it as a texture 310
Using the canvas as a texture 310
Using the canvas as a bump map 312
Using the output from a video as a texture 314
Summary 316
Chapter 11: Custom Shaders and Render Postprocessing 317
Setting up Three.js for postprocessing 318
Creating THREE.EffectComposer 319
Configuring THREE.EffectComposer for postprocessing 320
Updating the render loop 320
Postprocessing passes 321
Simple postprocessing passes 322
Using THREE.FilmPass to create a TV-like effect 323
Adding a bloom effect to the scene with THREE.BloomPass 324
Output the scene as a set of dots 326
Showing the output of multiple renderers on the same screen 327
Advanced EffectComposer flows using masks 329
Using THREE.ShaderPass for custom effects 333
Simple shaders 335
Blurring shaders 338
Advanced shaders 340
Creating custom postprocessing shaders 342
Custom grayscale shader 342
Creating a custom bit shader 346
Summary 348
Chapter 12: Adding Physics and Sounds to Your Scene 351
Creating a basic Three.js scene 352
Material properties 358
Basic supported shapes 360

ontents
Using constraints to limit movement of objects 367
Using PointConstraint to limit movement between two points 368
Creating door-like constraints with HingeConstraint 370
Limiting movement to a single axis with SliderConstraint 372
Creating a ball-and-socket-joint-like constraint
with ConeTwistConstraint 375
Creating detailed control with DOFConstraint 377
Add sound sources to your scene 381
Summary 384
Index 385


