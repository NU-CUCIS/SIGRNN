# SIGRNN
SIGRNN: Synthetic Minority Instances Generation in Imbalanced Datasets Using a Recurrent Neural Network Approach

## Train SIGRNN
- To train SIGRNN run <code>main.py</code>. The script takes a set of inputs and can be executed as the following example:
<code>python main.py --cuda --nhid 1024 --dropout 0.5 --epochs 20 --batch_size 8 --nlayers 2  --data ./data/seer --bptt 11</code>
    - Flag descriptions:
        - <code>--code</code> is used for GPU execution. The GPU id can be set within the code.
        - <code>--nhid</code> is the number of hidden units.
        - <code>--droput</code> is the percentage of drouped out connections.
        - <code>--batch_size</code> is to specify the batch size.
        - <code>--data</code> is the folder where the data is saved.
            - 3 files need to be present under the directory <code>train.txt, test.txt, and valid.txt</code>
        - <code>--nlayers</code> is the number of hidden layers. The default cell is LSTM.
        - The model will be saved in <code>model.pt</code>

## Generate using SIGRNN
<code>generate.py</code>
