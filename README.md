
# sc2trainingg
> Package created to prototype and design a challenge recommender system for StarCraf2.


`sc2trainingg` is part of the doctoral research project "Encouraging Play Experience Expansion Through Machine-Learning-based Recommendations". This creative practice project revolves around the design of "SC2 Training Grounds", a challenge recommendation system for StarCraft II. 
This package and its documentation describe the system's main back-end processes and components. Its purpose is to inspire and validate the application's design based on the features and limitations of existing resources. 
Hence, this package includes components that illustrate and describe the following stages of the application:
    
1. Replay data ingestion and database building (see `load_config` and `ingest` modules).
2. Replay data pre-processing and cleaning (see `match_df` and `players_df` modules).
3. Player clustering (see `pclustering` module).
4. Training of player classification model (see `classifier` module).
5. Validation of the model (see `classifier_val` module)
6. Game challenge ingestion and database building (see `challenge_process` module).
7. Recommendation generation (see `recommender` module).

Based on these components, I can catalogue the information that I can use to inform the application's user experience design. Additionally, I can better understand the application requirements to integrate them organically to said experience. 

## Usage

Here I will describe the use of the package.
