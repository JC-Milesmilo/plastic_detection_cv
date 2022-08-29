from scripts.image_detect import model
from scripts.heatmap import heatmap

def main():
    print("--Plastic project--")

    new_model = model(best_pt = 'Exp11.pt')
    new_heatmap = heatmap()
    
    df_result = new_model.result_model()

    new_heatmap.get_map(df_result)


if __name__ == "__main__":
    main()