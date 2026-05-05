# Prompt Design Rationale

## Project Context

This Generative AI component supports a student depression and lifestyle prediction system. The supervised model predicts whether a student is at risk of depression or not at risk. The Generative AI model then converts that prediction into understandable lifestyle and academic advice.

The prompt engineering part was designed to compare four different prompt styles and evaluate how each style affects the quality of the generated advice.

## Model Selection

The Gemini API was selected because it can generate clear, context-aware, and human-readable responses. The selected model was `gemini-2.5-flash`.

This model was suitable for the project because the system deals with sensitive student lifestyle and mental health-related predictions. The generated output must be supportive, clear, and safe.

## API Key Handling

The API key is not written directly in the notebook or source code. Instead, it is stored in a local `.env` file and loaded using `python-dotenv`.

The `.env` file is excluded from GitHub using `.gitignore`. A template file is provided so team members can understand how to configure their own environment without exposing private keys.

## Input Features Used in Prompts

The prompts use the following student features:

- CGPA
- Sleep Duration
- Study Hours
- Social Media Hours
- Physical Activity
- Stress Level
- Prediction Result

These features were selected because they are directly related to the prediction and help the model generate personalized advice.

## Template 1: Basic Lifestyle Advice

### Intended Use
This template provides a simple explanation and basic advice.

### Rationale
It is useful for users who need a short and easy-to-understand response. The structure is flexible, but the output may be less detailed than other templates.

### Strengths
- Simple
- Easy to read
- Good for quick advice

### Limitations
- Less organized
- May not provide enough detail for deeper analysis

## Template 2: Structured Mental Health and Academic Advice

### Intended Use
This template produces a structured response with clear sections.

### Rationale
It improves consistency by forcing the model to respond using the same categories: explanation, risk factors, lifestyle recommendations, and study balance advice.

### Strengths
- Very organized
- Easy to compare across test cases
- Covers both lifestyle and academic advice

### Limitations
- Can be long
- May feel less personal than a coaching-style response

## Template 3: Personalized Student Coach

### Intended Use
This template generates a supportive and encouraging response.

### Rationale
It focuses on personalized advice, daily action steps, and encouragement. This makes it useful for student-facing systems where tone matters.

### Strengths
- Supportive tone
- Personalized advice
- Includes actionable daily steps

### Limitations
- May be less analytical
- Output can become emotional or too long

## Template 4: Data-Driven Explanation

### Intended Use
This template explains why the prediction happened.

### Rationale
It supports interpretability by connecting the prediction result to the input features. This is important because users should understand which factors affected the prediction.

### Strengths
- Strong explanation
- Good interpretability
- Clearly identifies priority improvements

### Limitations
- Less emotionally supportive
- May sound more technical

## Testing Process

Each prompt template was tested using three test cases:

1. A high-risk student profile
2. A low-risk student profile
3. A moderate/high-risk student profile

This satisfies the requirement to test each template using multiple examples.

## Comparison Criteria

The generated responses were compared using the following criteria:

- Relevance to the prediction
- Detail and completeness
- Clarity and readability
- Personalization
- Safety and factual accuracy
- Response length
- Keyword alignment with the domain

## Best Prompt Selection

Template 2 was selected as the best overall prompt because it provides the most complete and organized response. It covers the prediction explanation, risk factors, recommendations, and study balance advice.

Template 3 was also strong because it gave supportive and personalized advice, but Template 2 was more consistent for evaluation and documentation.

## Integration Plan

In the final system, the supervised learning model will predict whether the student is at risk of depression. Then, the selected prompt template will send the prediction and student features to Gemini. Gemini will generate a clear explanation and lifestyle advice based on the prediction.

## Ethical Considerations

The system must not diagnose depression. The prediction should only be described as a risk indicator. The generated advice should encourage healthy habits and recommend professional or university support when needed.

The system should avoid harmful, judgmental, or overly confident language. Since mental health is sensitive, all responses must remain supportive and cautious.

## Lessons Learned

Prompt structure strongly affects output quality. Structured prompts produce more consistent responses, while personalized prompts produce warmer and more supportive advice. Safety instructions are necessary to prevent the model from treating the prediction as a clinical diagnosis.