# The Art of RENN

## Challenge Description

-  **Category:** Reverse Engineering
-  **Points:** 500
-  **Author:** aseng

How to train your flag guesser with hopes of improbable overfit deep learning?

![Challenge Image](https://i.imgur.com/g20UESY.png)
![First Blood](https://i.imgur.com/nrdvyY8.png)

## Flag Format

The flag is in the format: `gemastik{...}`

MD5(flag) = bfa1d885956a9ee88017d2b05b23b4ed

## Hint

<details>
<summary>View Hint</summary>

This is a preprocessed neural network but how does the model works in math? Attacker could gain advantage when they know this model architecture is vulnerable to {{something that you need to research}}

## Notes

You can run with any PyTorch version but you'll yield a slightly different discrepancy of the target float data (and this is fine). Preferrably use the same version if you want to deal with exact data.
</details>

## Files

- `chall.py`
