# index --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

<DOCTYPE html>

    <html>
    
    <head>
        <title> Tarayıcıda görünecek sekmenin adı </title>
        <link rel = "stylesheet" href = "style.css">
        
    </head>
    <body>
        <h1> PARLAK BİR GELECEK İÇİN YAPABİLECEKLERİNİZ </h1>
            <ul>
                <p> 1. Çöplerini yere değil çöp kutusuna atabilirsin. </p>
                <p> </p>
                <p> 2. Geri dönüştürülebilen maddeleri çöp kutusuna değil geri dönüşüm kutusuna atabilirsin. </p>
                <p> </p>
                <p> 3. En ufak tasarruftan bile kaçınmamalısın. örneğin(ellerini yıkarken suyu az açabilir <br>
                    veya gündüzleri ışıkları kapatabilirsin). </p>
                <p> </p>
                <p> 4. Hava kirliliğini azaltmak amacıyla elektrikli araçlara geçiş yapabilir, toplu taşıma <br>
                    araçlarını daha sık kullanmaya özen gösterebilir, bisiklet gibi çevre dostu araçlar kullanabilir <br>
                    veya yenilenebilir enerji kaynaklarına örneğin(güneş, rüzgar, hidroelektrik) gibi kaynaklara <br>
                    yatırım yapabilirsin. </p>
                <p> </p>
                <p> 5. Eğer bitki yetiştiriyorsan doğal gübreler ve kompost kullanarak toprak kirliliğini önleyebilir <br>
                    ve verimliliği arttırabilirsin. </p>
                <p> </p>
                <p> 6. Gürültü kirliliğini azaltmak için araç egzoz sistemlerini düzenleyerek <br>
                    veya gürültü seviyesi düşük makineler ve ekipmanlar kullanarak ses kirliliği <br>
                    sınırlarına uyabilirsin. </p>
                <p> </p>
                <p> 7. Enerji tasarrufu yapmak için yenilenebilir enerji projelerini destekleyebilir veya böyle <br>
                    projeler düzenleyebilirsiniz. </p>
                <p> </p>
                <p> 8. Toprak kirliliğini azaltmak için tek kullanımlık plastik gibi atıkları kullanmayabilir <br>
                    veya daha az kullanmaya çalışabilirsin. </p>
                <p> </p>
                <p> 9. Heyelan(toprak kayması) gibi doğal afetleri önlemek ve yaşam verimliliğini arttırmak amacıyla etrafı <br>
                    ağaçlandırarak yeşil alanları arttırabilirsin. </p>
                <p> </p>
                <p> 10. Bunlar ve diğer çevre kirliliğini azaltma kurallarını başkalarıyla paylaşarak <br>
                    etrafındakileri bilinçlendirebilir ve çevreyle uyum içerisinde yaşamalarını sağlayabilirsin. </p>
            </ul>

    </body>
    
    </html>

    <div id = "clock" ></div>
    <script>
        function updateClock() {
            const clock = document.getElementById("clock");
            const now = new Date();
            const hours = String(now.getHours()).padStart(2,"0");
            const minutes = String(now.getMinutes()).padStart(2,"0");
            const seconds = String(now.getSeconds()).padStart(2,"0");
            clock.innerText = `${hours}:${minutes}:${seconds}`;
        }
    
        setInterval(updateClock,1000);
        updateClock();
    </script>

# style --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

h1 {
    font-size: 35px;
    font-family: Arial, sans-serif;
    animation: color-change 6s infinite ease-in-out;
    text-align: center;
    padding: 20px;
    background-color: #212421;
    border-radius: 10px;
}

body {
    font-family: Arial, sans-serif;
    font-size: 21.5px;
    background-color: #212421;
    color: #ffffff;
    margin: 0;
    padding: 0;
}

ul p {
    transition: background-color 0.3s ease, color 0.3s ease;
}

ul p:hover {
    color: #8b8282;
}

@keyframes color-change {
    0% {
        color: rgb(0, 247, 255);
    }

    20% {
        color: rgb(43, 255, 0);
    }

    40% {
        color: red;
    }

    60% {
        color: rgb(251, 255, 0);
    }

    80% {
        color: rgb(255, 0, 212);
    }

    100% {
        color: rgb(0, 247, 255);
    }
}

#clock {
    position: absolute;
    top: 10px;
    right: 10px;
    font-size: 20px;
    color: #ffffff;
    background-color: #333131;
    padding: 8px 12px;
    border-radius: 5px;
}

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
