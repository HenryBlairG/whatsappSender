const puppeteer = require('puppeteer');


class Whatsapp {

    constructor() {
        
    }
}


module.exports = {
    run: async () => {
        puppeteer
            .launch({ headless: false })
            .then(browser => browser.newPage())
            .then(page => {
                page.setViewport({
                    width: 1280,
                    height: 800,
                    isMobile: false
                });
                page.goto('https://youtube.com', {
                    waitUntil: "networkidle2"
                });
            })
            .catch((err) => console.error(err));
    }
};