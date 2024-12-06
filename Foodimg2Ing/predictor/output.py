import os
import pickle
import torch
from torchvision import transforms
from tensorflow.keras.preprocessing import image
from PIL import Image
from args import get_parser
from model import get_model
from utils.output_utils import prepare_output

# Initialize once
data_dir = os.path.join(os.path.dirname(__file__), '..', 'predictor', 'models')

# Load vocabularies once
ingrs_vocab = pickle.load(open(os.path.join(data_dir, 'ingr_vocab.pkl'), 'rb'))
vocab = pickle.load(open(os.path.join(data_dir, 'instr_vocab.pkl'), 'rb'))
ingr_vocab_size = len(ingrs_vocab)
instrs_vocab_size = len(vocab)

#print(ingrs_vocab)
#print(vocab)

# Load model once
use_gpu = True
device = torch.device('cuda' if torch.cuda.is_available() and use_gpu else 'cpu')
map_loc = None if torch.cuda.is_available() and use_gpu else 'cpu'

args = get_parser()
args.maxseqlen = 15
args.ingrs_only = False
model = get_model(args, ingr_vocab_size, instrs_vocab_size)

model_path = os.path.join(data_dir, 'modelbest.ckpt')
model.load_state_dict(torch.load(model_path, map_location=map_loc, weights_only=True))
model.to(device)
model.eval()


# Define image transformations
to_input_transf = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.485, 0.456, 0.406), (0.229, 0.224, 0.225))
])

transform = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224)
])

def output(uploadedfile):
#     """Generate recipe predictions from an uploaded image file."""
    img = image.load_img(uploadedfile)
    image_transf = transform(img)
    image_tensor = to_input_transf(image_transf).unsqueeze(0).to(device)

    greedy = [True, True, False]
    beam = [-1, -1, -1]
    temperature = 1.0
    numgens = len(greedy)

    recipes = []

    for i in range(numgens):
        with torch.no_grad():
            outputs = model.sample(
                image_tensor,
                greedy=greedy[i],
                temperature=temperature,
                beam=beam[i],
                true_ingrs=None
            )

        ingr_ids = outputs['ingr_ids'].cpu().numpy()
        recipe_ids = outputs['recipe_ids'].cpu().numpy()

        outs, valid = prepare_output(recipe_ids[0], ingr_ids[0], ingrs_vocab, vocab)

        if valid['is_valid']:
            recipes.append({
            'title' : outs['title'],
            'ingredients' : outs['ingrs'],
            'instructions': outs['recipe']
            })
        else:
            continue
            # recipes.append({
            # 'title' : "Not a valid recipe!",
            # 'Error' : "Reason: " + valid['reason']
            # })

    return recipes

