##fetch-method
------------------
<custom-data src="https://hedefsite.com"></custom-data>

<script>
class CustomData extends HTMLElement {
    constructor() {
        super();
        this.attachShadow({ mode: "open" });
    }

    connectedCallback() {
        const url = this.getAttribute("src");
        fetch(url)
            .then(response => response.text())
            .then(data => {
                const wrapper = document.createElement("div");
                wrapper.innerHTML = data;
                this.shadowRoot.appendChild(wrapper);
            })
            .catch(error => console.error("Veri çekme hatası:", error));
    }
}

customElements.define("custom-data", CustomData);
</script>
---------------

Node.js Proxy api
---------------------
const express = require("express");
const cors = require("cors");
const axios = require("axios");

const app = express();
app.use(cors());

app.get("/proxy", async (req, res) => {
    try {
        const response = await axios.get("https://hedefsite.com");
        res.send(response.data);
    } catch (error) {
        res.status(500).send("Hata oluştu.");
    }
});

app.listen(3000, () => console.log("Proxy çalışıyor: http://localhost:3000"));
--------------------------------


##Web-Component -Proxy

------------

<real-time-data url="http://localhost:3000/proxy"></real-time-data>

<script>
class RealTimeData extends HTMLElement {
    constructor() {
        super();
        this.attachShadow({ mode: "open" });
    }

    connectedCallback() {
        this.loadData();
        setInterval(() => this.loadData(), 5000); // 5 saniyede bir güncelle
    }

    async loadData() {
        const url = this.getAttribute("url");
        try {
            const response = await fetch(url);
            const data = await response.text();
            this.shadowRoot.innerHTML = `<div>${data}</div>`;
        } catch (error) {
            console.error("Veri alınamadı:", error);
        }
    }
}

customElements.define("real-time-data", RealTimeData);
</script>

----------------

##Web Socket 

<real-time-websocket url="wss://hedefsite.com/socket"></real-time-websocket>

<script>
class RealTimeWebSocket extends HTMLElement {
    constructor() {
        super();
        this.attachShadow({ mode: "open" });
        this.socket = null;
    }

    connectedCallback() {
        const url = this.getAttribute("url");
        this.socket = new WebSocket(url);

        this.socket.onmessage = (event) => {
            this.shadowRoot.innerHTML = `<div>${event.data}</div>`;
        };
    }

    disconnectedCallback() {
        if (this.socket) this.socket.close();
    }
}

customElements.define("real-time-websocket", RealTimeWebSocket);
</script>
------------------------------------------

#SAMPLE FETCH...

async function getStockData() {
    const response = await fetch("https://bigpara.hurriyet.com.tr/borsa/canli-borsa/");
    const text = await response.text();

    // HTML içeriğini parse et
    const parser = new DOMParser();
    const doc = parser.parseFromString(text, "text/html");

    // İlgili div'in içeriğini al
    const stockData = doc.querySelector("#content > div > div.contentLeft > div > div.wideContent.sort-bar-x > div.liveStockBar.liveStockFilterBar > div.latestDataTime");

    console.log(stockData ? stockData.innerText : "Veri bulunamadı.");
}

getStockData();
----------------------------------

### 
npm init -y
npm install express axios cheerio cors
####


###
const express = require("express");
const axios = require("axios");
const cheerio = require("cheerio");
const cors = require("cors");

const app = express();
app.use(cors());

app.get("/borsa", async (req, res) => {
    try {
        const url = "https://bigpara.hurriyet.com.tr/borsa/canli-borsa/";
        const response = await axios.get(url);
        const $ = cheerio.load(response.data);

        // İstenen div'in içeriğini al
        const stockData = $("#content > div > div.contentLeft > div > div.wideContent.sort-bar-x > div.liveStockBar.liveStockFilterBar > div.latestDataTime").text();

        res.json({ data: stockData.trim() });
    } catch (error) {
        res.status(500).json({ error: "Veri çekme hatası" });
    }
});

app.listen(3000, () => console.log("Proxy çalışıyor: http://localhost:3000"));


####
