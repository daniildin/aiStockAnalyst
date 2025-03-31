document.addEventListener("DOMContentLoaded", function () {
   const form = document.querySelector("#stock-form");
   const stockInfoDiv = document.querySelector("#stock-info");

   form.addEventListener("submit", async function (event) {
       event.preventDefault();  

       const ticker = document.querySelector("#ticker").value.trim().toUpperCase();
       if (!ticker) {
           alert("Please enter a stock ticker.");
           return;
       }

       stockInfoDiv.innerHTML = "<p class='loading'>Fetching stock data...</p>";

       try {
           const response = await fetch("/get_stock", {
               method: "POST",
               headers: { "Content-Type": "application/json" },
               body: JSON.stringify({ ticker })
           });

           const data = await response.json();

           if (data.error) {
               stockInfoDiv.innerHTML = `<h3 class='error'>Error: ${data.error}</h3>`;
               return;
           }

           let stockHTML = `
               <div class="stock-card">
                   <h2>${data.stock.name} (${data.stock.symbol})</h2>
                   <p><strong>Price:</strong> $${data.stock.price}</p>
                   <p><strong>Market Cap:</strong> ${data.stock.market_cap}</p>
                   <p><strong>P/E Ratio:</strong> ${data.stock.pe_ratio}</p>
                   <p><strong>Dividend Yield:</strong> ${data.stock.dividend_yield}</p>
               </div>

               <h3>Stock Price History (Last Month)</h3>
               <ul class="history-list">
           `;

           for (const [date, price] of Object.entries(data.stock.history)) {
               stockHTML += `<li>${date}: <strong>$${price}</strong></li>`;
           }
           stockHTML += "</ul>";

           stockInfoDiv.innerHTML = stockHTML;
       } catch (error) {
           stockInfoDiv.innerHTML = `<h3 class='error'>Error fetching stock data</h3>`;
           console.error("Error:", error);
       }
   });
});
