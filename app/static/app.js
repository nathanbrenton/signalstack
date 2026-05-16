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
