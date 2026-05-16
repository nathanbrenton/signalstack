const healthButton = document.getElementById("health-button");

const healthOutput = document.getElementById("health-output");


healthButton.addEventListener("click", async () => {
    healthOutput.textContent = "Loading...";

    try {
        const response = await fetch("/api/v1/ml/health");

        const data = await response.json();

        healthOutput.textContent = JSON.stringify(
            data,
            null,
            2
        );
    } catch (error) {
        healthOutput.textContent =
            "Error connecting to API.";
    }
});

const keywordSearchButton = document.getElementById(
    "keyword-search-button"
);

const keywordSearchInput = document.getElementById(
    "keyword-search-input"
);

const keywordSearchResults = document.getElementById(
    "keyword-search-results"
);


keywordSearchButton.addEventListener("click", async () => {
    const query = keywordSearchInput.value.trim();

    if (!query) {
        keywordSearchResults.textContent =
            "Please enter a search term.";

        return;
    }

    keywordSearchResults.textContent = "Loading...";

    try {
        const response = await fetch(
            `/api/v1/articles?search=${encodeURIComponent(query)}`
        );

        const data = await response.json();

        if (!data.data || data.data.length === 0) {
            keywordSearchResults.textContent =
                "No articles found.";

            return;
        }

        keywordSearchResults.innerHTML = "";

        data.data.forEach((article) => {
            const articleDiv = document.createElement("div");

            articleDiv.className = "article-card";

        articleDiv.innerHTML = `
            <h3>${article.title}</h3>

            <div class="article-meta">
                Source: ${article.source}
            </div>

            <div class="article-summary">
                ${article.summary || ""}
            </div>
        `;

            keywordSearchResults.appendChild(articleDiv);
        });
    } catch (error) {
        keywordSearchResults.textContent =
            "Error performing search.";
    }
});

const semanticSearchButton = document.getElementById(
    "semantic-search-button"
);

const semanticSearchInput = document.getElementById(
    "semantic-search-input"
);

const semanticSearchResults = document.getElementById(
    "semantic-search-results"
);


semanticSearchButton.addEventListener("click", async () => {
    const query = semanticSearchInput.value.trim();

    if (!query) {
        semanticSearchResults.textContent =
            "Please enter a semantic search query.";

        return;
    }

    semanticSearchResults.textContent = "Loading...";

    try {
        const response = await fetch(
            `/api/v1/articles/semantic-search?query=${encodeURIComponent(query)}`
        );

        const data = await response.json();

        if (!data.results || data.results.length === 0) {
            semanticSearchResults.textContent =
                "No semantic matches found.";

            return;
        }

        semanticSearchResults.innerHTML = "";

        data.results.forEach((article) => {
            const articleDiv = document.createElement("div");

            articleDiv.className = "article-card";

                articleDiv.innerHTML = `
                    <h3>${article.title}</h3>
        
                    <div class="article-meta">
                        Similarity: ${article.similarity.toFixed(3)}
                        |
                        ML Category: ${article.ml_category || "unknown"}
                        |
                        ML Confidence: ${article.ml_confidence ?? "unknown"}
                    </div>
                `;

            semanticSearchResults.appendChild(articleDiv);
        });
    } catch (error) {
        semanticSearchResults.textContent =
            "Error performing semantic search.";
    }
});

const hybridSearchButton = document.getElementById(
    "hybrid-search-button"
);

const hybridSearchInput = document.getElementById(
    "hybrid-search-input"
);

const hybridSearchResults = document.getElementById(
    "hybrid-search-results"
);


hybridSearchButton.addEventListener("click", async () => {
    const query = hybridSearchInput.value.trim();

    if (!query) {
        hybridSearchResults.textContent =
            "Please enter a hybrid search query.";

        return;
    }

    hybridSearchResults.textContent = "Loading...";

    try {
        const response = await fetch(
            `/api/v1/articles/hybrid-search?query=${encodeURIComponent(query)}`
        );

        const data = await response.json();

        if (!data.results || data.results.length === 0) {
            hybridSearchResults.textContent =
                "No hybrid matches found.";

            return;
        }

        hybridSearchResults.innerHTML = "";

        data.results.forEach((article) => {
            const articleDiv = document.createElement("div");

            articleDiv.className = "article-card";

            articleDiv.innerHTML = `
                <h3>${article.title}</h3>

                <div class="article-meta">
                    Hybrid Score:
                    ${article.hybrid_score.toFixed(3)}

                    |
            
                    Semantic Similarity:
                    ${article.semantic_similarity.toFixed(3)}

                    |

                    ML Category:
                    ${article.ml_category || "unknown"}

                    |

                    ML Confidence:
                    ${
                        article.ml_confidence !== null
                            ? article.ml_confidence.toFixed(3)
                            : "unknown"
                    }
                </div>
            `;

            hybridSearchResults.appendChild(articleDiv);
        });
    } catch (error) {
        hybridSearchResults.textContent =
            "Error performing hybrid search.";
    }
});

const mlPredictButton = document.getElementById(
    "ml-predict-button"
);

const mlPredictInput = document.getElementById(
    "ml-predict-input"
);

const mlPredictOutput = document.getElementById(
    "ml-predict-output"
);


mlPredictButton.addEventListener("click", async () => {
    const text = mlPredictInput.value.trim();

    if (!text) {
        mlPredictOutput.textContent =
            "Please enter article text.";

        return;
    }

    mlPredictOutput.textContent = "Loading...";

    try {
        const response = await fetch(
            "/api/v1/ml/predict",
            {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({
                    text: text,
                }),
            }
        );

        const data = await response.json();

        mlPredictOutput.textContent = JSON.stringify(
            data,
            null,
            2
        );
    } catch (error) {
        mlPredictOutput.textContent =
            "Error performing ML prediction.";
    }
});

const relatedArticlesButton = document.getElementById(
    "related-articles-button"
);

const relatedArticleIdInput = document.getElementById(
    "related-article-id-input"
);

const relatedArticlesResults = document.getElementById(
    "related-articles-results"
);


relatedArticlesButton.addEventListener("click", async () => {
    const articleId = relatedArticleIdInput.value.trim();

    if (!articleId) {
        relatedArticlesResults.textContent =
            "Please enter an article ID.";

        return;
    }

    relatedArticlesResults.textContent = "Loading...";

    try {
        const response = await fetch(
            `/api/v1/articles/${articleId}/similar`
        );

        const data = await response.json();

        if (!data.results || data.results.length === 0) {
            relatedArticlesResults.textContent =
                "No related articles found.";

            return;
        }

        relatedArticlesResults.innerHTML = "";

        data.results.forEach((article) => {
            const articleDiv = document.createElement("div");

            articleDiv.className = "article-card";

            articleDiv.innerHTML = `
                <h3>${article.title}</h3>

                <div class="article-meta">
                    Similarity:
                    ${article.similarity.toFixed(3)}

                    |

                    ML Category:
                    ${article.ml_category || "unknown"}
                </div>
            `;

            relatedArticlesResults.appendChild(articleDiv);
        });
    } catch (error) {
        relatedArticlesResults.textContent =
            "Error loading related articles.";
    }
});
