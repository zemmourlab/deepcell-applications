# deepcell-applications available offline


This repo is a fork of the https://github.com/vanvalenlab/deepcell-applications repository with the option to add the path to the model.
Thus, the programm can be run without anyinternet connection needed.

A script and runnable Docker image for plugging DeepCell Applications (like `Mesmer`) into existing pipelines.

## Running the Python script

The `run_app.py` script is used to read the input files from the user and process them with the selected Application.
An example Python script `run_app.py` is provided as an example `deepcell.applications` workflow.

### Script arguments

The first required argument to the script is the Application name: `python run_app.py APP_NAME`.
Each supported application has a variety of different configuration arguments.
Below is a table summarizing the currently supported applications and their arguments and any defaults.
For more information, use `python run_app.py --help` or `python run_app.py APP_NAME --help`.

To learn more about the pretrained models, see the [introductory documentation](https://github.com/vanvalenlab/intro-to-deepcell/tree/master/pretrained_models).

#### Mesmer arguments

| Name                 | Description | Default Value |
|:---------------------| :--- | :--- |
| `--output-directory` | Directory to save output file. | `"./output"` |
| `--output-name`      | The name for the output file. | `"mask.tif"` |
| `--nuclear-image`    | **REQUIRED**: The path to an image containing the nuclear marker(s). | `""` |
| `--nuclear-channel`  | The numerical index of the channel(s) from `nuclear-image` to select. If multiple values are passed, the channels will be summed. | `0` |
| `--membrane-image`   | The path to an image containing the membrane marker(s). If not passed, an array of zeroes will be used instead. | `""` |
| `--membrane-channel` | The numerical index of the channel(s) from `membrane-image` to select. If multiple values are passed, the channels will be summed. | `0` |
| `--compartment`      | Predict nuclear or whole-cell segmentation. | `"whole-cell"` |
| `--image-mpp`        | The resolution of the image in microns-per-pixel. A value of 0.5 corresponds to 20x zoom. | `0.5` |
| `--batch-size`       | Number of images to predict on per batch. | `4` |
| `--squeeze`          | Whether to `np.squeeze` the outputs before saving as a tiff. | `False` |
| `--model-path`       | The path of the model loaded | `None` |

### Script command

```bash
export DATA_DIR=/path/to/example_data/multiplex
export APPLICATION=mesmer
export NUCLEAR_FILE=example_nuclear_image.tif
export MEMBRANE_FILE=example_membrane_image.tif
export PATH_MODEL=/path/to/model
python run_app.py $APPLICATION \
  --nuclear-image $DATA_DIR/$NUCLEAR_FILE \
  --nuclear-channel 0 \
  --membrane-image $DATA_DIR/$MEMBRANE_FILE \
  --membrane-channel 0 1 \
  --output-directory $DATA_DIR \
  --output-name mask.tif \
  --compartment whole-cell \
  --model-path $PATH_MODEL
```
