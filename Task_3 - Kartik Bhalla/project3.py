import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def load_data():
    try:
        df = pd.read_csv("raw_skills.csv")
        return df
    except FileNotFoundError:
        print("Error: raw_skills.csv file not found.")
        exit()


def get_user_input():
    print("\n=== AI Tech Stack Recommendation System ===")
    print("Enter at least 3 skills/interests.")
    print("Type 'done' when finished.\n")

    skills = []

    while True:
        skill = input("Enter skill: ").strip()

        if skill.lower() == "done":
            if len(skills) < 3:
                print("Please enter at least 3 skills.")
                continue
            break

        if skill:
            skills.append(skill)

    return " ".join(skills)


def recommend_roles(user_input, df):
    all_text = df["Skills"].tolist()
    all_text.append(user_input)

    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(all_text)

    user_vector = tfidf_matrix[-1]
    role_vectors = tfidf_matrix[:-1]

    similarity_scores = cosine_similarity(user_vector, role_vectors)

    df["Similarity"] = similarity_scores[0]

    recommendations = df.sort_values(
        by="Similarity",
        ascending=False
    )

    return recommendations


def display_results(recommendations):
    print("\n=== Top Career Recommendations ===\n")

    top_n = 5

    for i, (_, row) in enumerate(recommendations.head(top_n).iterrows(), start=1):
        print(f"{i}. {row['Role']}")
        print(f"   Match Score: {row['Similarity']:.2f}")
        print(f"   Required Skills: {row['Skills']}")
        print()


def main():
    df = load_data()

    user_input = get_user_input()

    recommendations = recommend_roles(user_input, df)

    display_results(recommendations)


if __name__ == "__main__":
    main()