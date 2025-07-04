# DeepGesture - A conversational gesture synthesis system based on emotions and semantic

## Abstract

> Along with the explosion of large language models, improvements
    in speech synthesis, advancements in hardware, and the evolution
    of computer graphics, the current bottleneck in creating digital
    humans lies in generating character movements that correspond
    naturally to text or speech inputs.
    In this work, we present DeepGesture, a diffusion-based gesture
    synthesis framework for generating expressive co-speech gestures
    conditioned on multimodal signals—text, speech, emotion, and seed
    motion. Built upon the DiffuseStyleGesture model, DeepGesture
    introduces novel architectural enhancements that improve semantic alignment and emotional expressiveness
    in generated gestures.
    Specifically, we integrate fast text transcriptions as semantic conditioning and implement emotion-guided
    classifier-free diffusion
    to support controllable gesture generation across affective states.
    A lightweight Transformer backbone combines full self-attention
    and cross-local attention for effective feature fusion of heterogeneous modalities. To visualize results,
    we implement a full rendering pipeline in Unity based on BVH output from the model.
    Evaluation on the ZeroEGGS dataset shows that DeepGesture produces gestures with improved human-likeness
    and contextual appropriateness, outperforming baselines on Mean Opinion Score and
    Fréchet Gesture Distance metrics. Our system supports interpolation between emotional states and
    demonstrates generalization to
    out-of-distribution speech, including synthetic voices—marking a
    step forward toward fully multimodal, emotionally aware digital humans.

![DeepGesture](/static/figures/DeepGesture.png)
