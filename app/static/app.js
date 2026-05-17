// SignalStack frontend controller.
// This file connects the static demo UI to the FastAPI backend endpoints.


// Helper functions

function formatTimestamp(timestamp) {
    if (!timestamp) {
        return "Never";
    }

    const date = new Date(timestamp);

    return date.toLocaleString();
}

function createTimingDiv(resultCount, duration) {
    const timingDiv = document.createElement("div");

    timingDiv.className = "article-meta";

    timingDiv.textContent =
        `Results: ${resultCount} | ` +
        `Frontend Fetch Time: ${duration} ms`;

    return timingDiv;
}


function formatNumber(value) {
    if (value === null || value === undefined) {
        return "unknown";
    }

    return Number(value).toFixed(3);
}


function createArticleTitle(article) {
    if (!article.url) {
        return `<h3>${article.title}</h3>`;
    }

    return `
        <h3>
            <a
                href="${article.url}"
                target="_blank"
                rel="noopener noreferrer"
                class="article-link"
            >
                ${article.title}
            </a>
        </h3>
    `;
}

function addEnterKeyListener(inputElement, callback) {
    inputElement.addEventListener("keydown", (event) => {
        if (event.key === "Enter") {
            callback();
        }
    });
}

function createStatCard(label, value) {
    const statCard = document.createElement("div");

    statCard.className = "stat-card";

    statCard.innerHTML = `
        <div class="stat-value">
            ${value}
        </div>

        <div class="stat-label">
            ${label}
        </div>
    `;

    return statCard;
}




// System health check

const healthButton = document.getElementById("health-button");
const healthOutput = document.getElementById("health-output");

healthButton.addEventListener("click", async () => {
    healthOutput.textContent = "Loading...";

    try {
        const response = await fetch("/api/v1/ml/health");
        const data = await response.json();

        healthOutput.textContent = JSON.stringify(data, null, 2);
    } catch (error) {
        healthOutput.textContent = "Error connecting to API.";
    }
});


// Article keyword search

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

    const startTime = performance.now();

    try {
        const response = await fetch(
            `/api/v1/articles?search=${encodeURIComponent(query)}`
        );

        const data = await response.json();

        if (!data.data || data.data.length === 0) {
            keywordSearchResults.textContent = "No articles found.";
            return;
        }

        const endTime = performance.now();
        const duration = (endTime - startTime).toFixed(1);

        keywordSearchResults.innerHTML = "";

        keywordSearchResults.appendChild(
            createTimingDiv(data.data.length, duration)
        );

        data.data.forEach((article) => {
            const articleDiv = document.createElement("div");

            articleDiv.className = "article-card";

            articleDiv.innerHTML = `
                ${createArticleTitle(article)}

                <div class="article-meta">
                    Source: ${article.source || "unknown"}
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


// Semantic search

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

    const startTime = performance.now();

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

        const endTime = performance.now();
        const duration = (endTime - startTime).toFixed(1);

        semanticSearchResults.innerHTML = "";

        semanticSearchResults.appendChild(
            createTimingDiv(data.results.length, duration)
        );

        data.results.forEach((article) => {
            const articleDiv = document.createElement("div");

            articleDiv.className = "article-card";

            articleDiv.innerHTML = `
                ${createArticleTitle(article)}

                <div class="article-meta">
                    Similarity: ${formatNumber(article.similarity)}
                    |
                    ML Category: ${article.ml_category || "unknown"}
                    |
                    ML Confidence: ${formatNumber(article.ml_confidence)}
                </div>
            `;

            semanticSearchResults.appendChild(articleDiv);
        });
    } catch (error) {
        semanticSearchResults.textContent =
            "Error performing semantic search.";
    }
});


// Hybrid search

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

    const startTime = performance.now();

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

        const endTime = performance.now();
        const duration = (endTime - startTime).toFixed(1);

        hybridSearchResults.innerHTML = "";

        hybridSearchResults.appendChild(
            createTimingDiv(data.results.length, duration)
        );

        data.results.forEach((article) => {
            const articleDiv = document.createElement("div");

            articleDiv.className = "article-card";

            articleDiv.innerHTML = `
                ${createArticleTitle(article)}

                <div class="article-meta">
                    Hybrid Score: ${formatNumber(article.hybrid_score)}
                    |
                    Semantic Similarity:
                    ${formatNumber(article.semantic_similarity)}
                    |
                    ML Category: ${article.ml_category || "unknown"}
                    |
                    ML Confidence: ${formatNumber(article.ml_confidence)}
                </div>
            `;

            hybridSearchResults.appendChild(articleDiv);
        });
    } catch (error) {
        hybridSearchResults.textContent =
            "Error performing hybrid search.";
    }
});


// ML prediction

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

    const startTime = performance.now();

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

        const endTime = performance.now();
        const duration = (endTime - startTime).toFixed(1);

        mlPredictOutput.textContent =
            `Frontend Fetch Time: ${duration} ms\n\n` +
            JSON.stringify(data, null, 2);
    } catch (error) {
        mlPredictOutput.textContent =
            "Error performing ML prediction.";
    }
});


// Related articles

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

    const startTime = performance.now();

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

        const endTime = performance.now();
        const duration = (endTime - startTime).toFixed(1);

        relatedArticlesResults.innerHTML = "";

        relatedArticlesResults.appendChild(
            createTimingDiv(data.results.length, duration)
        );

        data.results.forEach((article) => {
            const articleDiv = document.createElement("div");

            articleDiv.className = "article-card";

            articleDiv.innerHTML = `
                ${createArticleTitle(article)}

                <div class="article-meta">
                    Similarity: ${formatNumber(article.similarity)}
                    |
                    ML Category: ${article.ml_category || "unknown"}
                </div>
            `;

            relatedArticlesResults.appendChild(articleDiv);
        });
    } catch (error) {
        relatedArticlesResults.textContent =
            "Error loading related articles.";
    }
});

addEnterKeyListener(
    keywordSearchInput,
    () => keywordSearchButton.click()
);

addEnterKeyListener(
    semanticSearchInput,
    () => semanticSearchButton.click()
);

addEnterKeyListener(
    hybridSearchInput,
    () => hybridSearchButton.click()
);

addEnterKeyListener(
    relatedArticleIdInput,
    () => relatedArticlesButton.click()
);


// RSS feed panel

const rssFeedsButton = document.getElementById("rss-feeds-button");
const rssPanel = document.getElementById("rss-panel");

const rssPanelCloseButton = document.getElementById(
    "rss-panel-close-button"
);

const rssFeedList = document.getElementById(
    "rss-feed-list"
);

const rssFeedInput = document.getElementById(
    "rss-feed-input"
);

const rssFeedAddButton = document.getElementById(
    "rss-feed-add-button"
);

const rssFeedMessage = document.getElementById(
    "rss-feed-message"
);

const rssSyncButton = document.getElementById(
    "rss-sync-button"
);

function renderRssFeedList(feeds) {
    rssFeedList.innerHTML = "";

    feeds.forEach((feed) => {
        const feedUrl = feed.url || "N/A";
        const lastIngested = formatTimestamp(
            feed.last_ingested_at
        );
        const lastError = feed.last_error || "None";

        const listItem = document.createElement("li");

        listItem.innerHTML = `
            <div class="rss-feed-item">
                <a
                    href="${feedUrl}"
                    target="_blank"
                    rel="noopener noreferrer"
                    class="article-link"
                >
                    ${feedUrl}
                </a>

                <div class="article-meta">
                    Active: ${feed.is_active}
                    |
                    Last Ingested: ${lastIngested}
                    |
                    Last Error: ${lastError}
                </div>
            </div>
        `;

        rssFeedList.appendChild(listItem);
    });
}

async function loadRssFeeds() {
    rssFeedList.innerHTML = "";

    try {
        const response = await fetch("/api/v1/rss-feeds");
        const data = await response.json();

        renderRssFeedList(data.feeds || []);
    } catch (error) {
        renderRssFeedList(["N/A"]);

        rssFeedMessage.textContent =
            "Unable to load RSS feeds. Displaying N/A.";
    }
}

async function syncRssFeeds() {
    rssFeedMessage.textContent =
        "Synchronizing RSS feed sources...";

    try {
        const response = await fetch(
            "/api/v1/rss-feeds/ingest",
            {
                method: "POST",
            }
        );

        const data = await response.json();

        rssFeedMessage.innerHTML =
            `
            <div>
                Processed: ${data.processed_count}
                |
                Successful: ${data.success_count}
                |
                Errors: ${data.error_count}
            </div>
            `;
        if (data.errors && data.errors.length > 0) {
            const errorList = document.createElement("ul");

            data.errors.forEach((item) => {
                const listItem = document.createElement("li");

                listItem.textContent =
                    `${item.url} | ${item.error}`;

                errorList.appendChild(listItem);
            });

            rssFeedMessage.appendChild(errorList);
        }

        loadRssFeeds();
        loadDashboardStats();
    } catch (error) {
        console.error(error);

        rssFeedMessage.textContent =
            `RSS synchronization failed: ${error.message}`;
    }
}

rssFeedsButton.addEventListener("click", () => {
    rssPanel.classList.remove("hidden");
    loadRssFeeds();
});

rssSyncButton.addEventListener("click", () => {
    syncRssFeeds();
});

rssPanelCloseButton.addEventListener("click", () => {
    rssPanel.classList.add("hidden");
});

const dashboardStats = document.getElementById("dashboard-stats");


async function loadDashboardStats() {
    try {
        const response = await fetch("/api/v1/dashboard/stats");
        const data = await response.json();

        dashboardStats.innerHTML = "";

        dashboardStats.appendChild(
            createStatCard("Total Articles", data.total_articles)
        );

        dashboardStats.appendChild(
            createStatCard("Active RSS Feeds", data.active_rss_feeds)
        );

        dashboardStats.appendChild(
            createStatCard(
                "ML-Classified Articles",
                data.ml_classified_articles
            )
        );

        dashboardStats.appendChild(
            createStatCard("Embedded Articles", data.embedded_articles)
        );

        dashboardStats.appendChild(
            createStatCard(
                "Last Article Ingest",
                formatTimestamp(data.last_article_ingested_at)
            )
        );

        dashboardStats.appendChild(
            createStatCard(
                "Last Feed Ingest",
                formatTimestamp(data.last_feed_ingest_at)
            )
        );

    } catch (error) {
        dashboardStats.innerHTML =
            `<div class="stat-card">Unable to load dashboard stats.</div>`;
    }
}


loadDashboardStats();
