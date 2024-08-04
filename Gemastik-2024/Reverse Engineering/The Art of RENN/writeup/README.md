# CTF Gemastik 2024 Writeup: The Art of RENN

## Challenge Description

We're presented with a machine learning model and its output. Our task is to reconstruct the input flag that produced this output. The challenge involves a model inversion attack on a neural network.

## Initial Analysis

Let's break down the key components of the provided `chall.py`:

1. A neural network (`sigma`) with three linear layers: 34 -> 496 -> 128 -> 24
2. A function `convert()` that transforms the flag string into a tensor of float values
3. Custom weight and bias initialization using `wb()` function
4. The output of the model when run on the hidden flag

## Concept

The core idea is to perform a model inversion attack. We'll use the known model architecture and its output to reconstruct the input that likely produced this output.

### Step 1: Understanding the Model

The model is a simple feed-forward neural network:
- Input size: 34 (matching the flag length)
- Hidden layers: 496 and 128 neurons
- Output size: 24 (matching the target output size)

### Step 2: Setting Up the Attack

1. We start with the known parts of the flag: "gemastik{" and "}".
2. We create a tensor for the unknown part, initialized randomly.
3. We set up an optimizer (Adam) to adjust this unknown part.

### Step 3: The Reconstruction Loop

In each iteration:
1. We create a full input by concatenating the known prefix, unknown part, and known suffix.
2. We pass this through the model and compare the output to the target output.
3. We calculate the loss and use backpropagation to adjust the unknown part.
4. We clamp the values to ensure they remain in the printable ASCII range.

### Step 4: Multiple Attempts

The code runs the reconstruction process multiple times with different random seeds to increase the chances of finding the correct flag.

## Implementation Details

Key parts of the implementation:

1. Flag reconstruction function:

```python
def reconstruct_flag(seed):
    torch.manual_seed(seed)
    known_prefix = "gemastik{"
    known_suffix = "}"
    unknown_length = 34 - len(known_prefix) - len(known_suffix)
    unknown_part = torch.randint(32, 127, (1, unknown_length), dtype=torch.float32, requires_grad=True)
    optimizer = optim.Adam([unknown_part], lr=0.01)
    # ... (optimization loop) ...
```

2. Loss calculation and optimization:

```python
output = model(full_input)
loss = criterion(output[0], target_output)
loss.backward()
optimizer.step()
```

3. Clamping values to printable ASCII range:

```python
with torch.no_grad():
    unknown_part.data.clamp_(32, 126)
```

## Solving the Challenge

To solve the challenge:

1. Run `solver.py` code.
2. The script will make multiple attempts to reconstruct the flag.
3. For each attempt, it will print the reconstructed flag and verify it using an MD5 hash.

## Flag Verification

The correct flag is verified using its MD5 hash:

```python
def verify_flag(result):
    import hashlib
    md5_hash = hashlib.md5(result.encode()).hexdigest()
    print("MD5 hash of the result:", md5_hash)
    print("Expected MD5 hash:      bfa1d885956a9ee88017d2b05b23b4ed")
    return md5_hash == "bfa1d885956a9ee88017d2b05b23b4ed"
```

## Conclusion

This challenge demonstrates a practical application of a model inversion attack. By leveraging knowledge of the model architecture and its output, we can reconstruct sensitive input data (in this case, a flag). This highlights the importance of protecting not just the model itself, but also its outputs, especially when dealing with sensitive information.

Flag: `gemastik{y0u_are_a_NN_m0del_pwn3r}`