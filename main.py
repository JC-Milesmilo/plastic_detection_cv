from scripts.image_detect import model
from scripts.geo_heatmap import mapbox
import os

def main():
    print("--Plastic project--")

    new_model = model(best_pt = 'Exp4.pt')
    new_heatmap = mapbox()
    
    dr = f'{os.getcwd()}\\resources\\img\\pre_processed\\'
    
    for i in os.listdir(dr):
        df_result = new_model.result_model(i)
        new_heatmap.get_map(df_result)

        # df_result = new_model.result_model(dirs[count])
        # #df_result = new_model.result_model()
        # count += 1
        # new_heatmap.get_map(df_result)


if __name__ == "__main__":
    main()