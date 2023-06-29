from deepcell.utils.plot_utils import create_rgb_image
import matplotlib.pyplot as plt
from deepcell.applications import Mesmer
from deepcell.utils.plot_utils import make_outline_overlay
import os


def cut_array_into_squares(arr, square_size):
    # Get the shape of the input array
    rows, cols = arr.shape[:2]

    # Calculate the number of rows and columns for complete squares
    num_rows = rows // square_size
    num_cols = cols // square_size

    # Calculate the remaining rows and columns
    remaining_rows = rows % square_size
    remaining_cols = cols % square_size

    # Create an empty list to store the squares
    squares = []

    # Iterate over each square and extract it from the array
    for row in range(num_rows):
        for col in range(num_cols):
            # Calculate the start and end indices for the current square
            start_row = row * square_size
            end_row = start_row + square_size
            start_col = col * square_size
            end_col = start_col + square_size

            # Extract the square from the array
            square = arr[start_row:end_row, start_col:end_col, :]

            # Append the square to the list
            squares.append(square)

    # Include the remaining rows in the last row of squares
    for col in range(num_cols):
        start_row = num_rows * square_size
        end_row = start_row + remaining_rows
        start_col = col * square_size
        end_col = start_col + square_size

        square = arr[start_row:end_row, start_col:end_col, :]
        squares.append(square)

    # Include the remaining columns in the last column of squares
    for row in range(num_rows):
        start_row = row * square_size
        end_row = start_row + square_size
        start_col = num_cols * square_size
        end_col = start_col + remaining_cols

        square = arr[start_row:end_row, start_col:end_col, :]
        squares.append(square)

    # Include the remaining square in the bottom right corner
    start_row = num_rows * square_size
    end_row = start_row + remaining_rows
    start_col = num_cols * square_size
    end_col = start_col + remaining_cols

    square = arr[start_row:end_row, start_col:end_col, :]
    squares.append(square)

    return squares


def segmentation_control(image, prediction, directory_output, square_size=5000):
    rgb_images = create_rgb_image(image, channel_colors=['green', 'blue'])
    os.makedirs(os.path.join(directory_output, 'controls'), exist_ok=True)
    # Running the prediction
    # print("Running the prediction...")
    overlay_data = make_outline_overlay(rgb_data=rgb_images, predictions=prediction)

    print("Saving the whole image...")
    plt.rcParams["figure.figsize"] = (12, 12)
    plt.imshow(overlay_data[0, ...])
    plt.title('Control segmentation', fontsize=15)
    plt.savefig(os.path.join(directory_output, 'controls', f'control_segmentation.png'), bbox_inches='tight', dpi=500)
    plt.close()

    print("Slicing the big image into squares...")
    squares = cut_array_into_squares(overlay_data[0], square_size)
    # print(squares[0].shape)
    # print(len(squares))

    print("Saving the squares...")
    for k in range(len(squares)):
        # plot the prediction
        overlay_data_square = squares[k]
        plt.rcParams["figure.figsize"] = (12, 12)
        plt.imshow(overlay_data_square)
        plt.title('Control segmentation', fontsize=15)
        plt.savefig(os.path.join(directory_output, 'controls', f'control_segmentation_{k + 1}.png'), bbox_inches='tight', dpi=500)
        plt.close()
        print(f"Square {k + 1}/{len(squares)} saved.")

# python3 /project/jfkfloor2/zemmourlab/loqmen/mcmicro_codex/codex-pipeline/controls/segmentation_controls.py
# def get_args():
#     parser = argparse.ArgumentParser(description="Segmentation of control images")
#     parser.add_argument("-i", "--image_path", required=True, help="Path to the image")
#     parser.add_argument("-m", "--markers_path", required=True, help="Path to the markers")
#     parser.add_argument("-o", "--path_output", required=True, help="Path to the output")
#     parser.add_argument("-s", "--square_size", required=False, default=5000, help="Size of the squares")
#     parser.add_argument("-mem", "--membrane_marker", required=True, help="Name of the membrane marker")
#     parser.add_argument("-nuc", "--nuclear_marker", required=True, help="Name of the nuclear marker")
#
#     return parser.parse_args()


# if __name__ == '__main__':
#     # image_path = "/project/jfkfloor2/zemmourlab/loqmen/mcmicro_codex/2022_12_07_F4_colon/illumination/" \
#     #              "2022_12_07_F4_colon_stitched_backsub_illcorrection.tif"
#     # markers_path = "/project/jfkfloor2/zemmourlab/loqmen/mcmicro_codex/2022_12_07_F4_colon/markers_bs.csv"
#     # path_output = "/project/jfkfloor2/zemmourlab/loqmen/mcmicro_codex/2022_12_07_F4_colon/segmentation/"
#     #
#     # membrane_marker = 'NaK_ATPase'
#     # nuclear_marker = 'Dapi_1'
#     args = get_args()
#     segmentation_control(args.image_path, args.markers_path, args.path_output, args.membrane_marker, args.nuclear_marker, square_size=args.square_size)
