<p align="center">
 <img src=maomao.gif />
</p>

<div style="display: flex; flex-wrap: wrap; gap: 16px; align-items: flex-start; justify-content: center">
    <style>
        #about-me {
            border: 1px solid #FFFFFF;
            border-radius: 8px;
            padding: 16px;
            width: 45%;
            background: #151515;
            font-size: 1.1em;
            box-shadow: 0 2px 8px rgba(74,144,226,0.08);
        }
        #about-me h2 {
            color: #fff;
            margin-top: 0.3em;
        }
        .responsive-row > div {
            flex: 1 1 0;
            display: flex;
            flex-direction: column;
        }
    </style>
    <div id="about-me" style="min-width: 320px; max-width: 500px;">
        <h2 align="center">About me</h2>
        <ul id='jokes'></ul>
        <script>
            async function fetchChuckNorrisJokes(name = "Your Name") {
                const jokesList = document.getElementById('jokes');
                jokesList.innerHTML = '';
                // Fetch the local chuckprogramming.txt file
                const res = await fetch('chuckprogramming.txt');
                const text = await res.text();
                const lines = text.split('\n').filter(line => line.trim());
                for (let i = 0; i < 3; i++) {
                    const randomIndex = Math.floor(Math.random() * lines.length);
                    const joke = lines[randomIndex].replace(/Chuck Norris/gi, name);
                    const jokeElem = document.createElement('li');
                    jokeElem.className = 'joke';
                    jokeElem.textContent = joke;
                    jokesList.appendChild(jokeElem);
                }
            }
            fetchChuckNorrisJokes("Mario");
        </script>
    </div>
    <div style="flex: 1; min-width: 320px; max-width: 500px;">
    <style>
        .tab {
            overflow: hidden;
            border: 1px solid #FFFFFF;
            background-color: #151515;
            width: 100%;
            height: 4em;
            display: flex;
            border-radius: 8px 8px 0 0;
        }
        .tab button {
            background-color: #151515;
            border: none;
            outline: none;
            cursor: pointer;
            padding: 14px 16px;
            transition: 0.3s;
            flex: 1;
            text-align: center;
            font-size: 1em;
            color: #FFFFFF;
        }
        .tab button:hover {
            background-color: #79ff97;
            color: #151515;
        }
        .tab button.active {
            background-color: #79ff97;
            color: #151515;
        }
        .tabcontent {
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            border: 1px solid #FFFFFF;
            border-radius: 0 0 8px 8px;
            border-top: none;
            width: 100%;
            min-height: 120px;
            height: 100%;
            animation: fadeEffect 1s;
            background: #151515;
            color: #9f9f9f;
        }
        @keyframes fadeEffect {
            from {opacity: 0;}
            to {opacity: 1;}
        }
        #Wisdom  {
            font-size: 1.2rem;
        }
        #WisdomInner {
            padding: 20px;
            display: flex;
            border: 1px solid #FFFFFF;
            align-items: center;
            text-align: center;
        }
        #Joke {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100%;
        }
        #Joke img {
            display: block;
            margin: auto;
            max-width: 100%;
            max-height: 100%;
        }
    </style>
    <div class="tab">
        <button class="tablinks" onclick="openTab(event, 'Wisdom')" id="defaultOpen">German Wisdom</button>
        <button class="tablinks" onclick="openTab(event, 'Joke')">Joke</button>
        <button class="tablinks" onclick="openTab(event, 'Quote')">Quote</button>
    </div>
    <div id="Wisdom" class="tabcontent">
        <div id="WisdomInner">
        </div>
    </div>
    <div id="Joke" class="tabcontent">
        <img src="https://readme-jokes.vercel.app/api?hideBorder&bgColor=%23151515&textColor=%239f9f9f&codeColor=%2379ff97&qColor=%239f9f9f&aColor=%2379ff97" />
    </div>
    <div id="Quote" class="tabcontent">
        <a href=https://github.com/piyushsuthar/github-readme-quotes>
            <img src=https://quotes-github-readme.vercel.app/api?type=horizontal&theme=dark />
        </a>
    </div>
    <script>
        document.getElementById("defaultOpen").click();
        function openTab(evt, tabName) {
            var i, tabcontent, tablinks;
            tabcontent = document.getElementsByClassName("tabcontent");
            for (i = 0; i < tabcontent.length; i++) {
                tabcontent[i].style.display = "none";
            }
            tablinks = document.getElementsByClassName("tablinks");
            for (i = 0; i < tablinks.length; i++) {
                tablinks[i].className = tablinks[i].className.replace(" active", "");
            }
            document.getElementById(tabName).style.display = "block";
            evt.currentTarget.className += " active";
            if (tabName == "Wisdom") displayRandomWisdom();
        }
        async function displayRandomWisdom() {
            const randomNumber = Math.floor(Math.random() * 851) + 1;
            const response = await fetch('https://raw.githubusercontent.com/Torfkopp/LapisDiscordBot/master/resources/wisdom.txt');
            const text = await response.text();
            const lines = text.split('\n');
            document.getElementById('WisdomInner').innerText = lines[randomNumber - 1] || 'No wisdom found.';
        }
    </script>
    </div>
</div>

### GitHub Analytics

<p align="center">
<a href="https://github.com/Torfkopp">
    <img height="200" align="center" src="https://github-readme-stats-eight-theta.vercel.app/api?username=Torfkopp&show_icons=true&theme=dark&include_all_commits=true&count_private=true"/>
    <img height="200" align="center" src="https://github-readme-stats-eight-theta.vercel.app/api/top-langs/?username=torfkopp&layout=compact&theme=dark&langs_count=8&hide=java"/>
</a>
</p>
<!-- <img src="https://data-card-for-spotify.herokuapp.com/api/card?user_id=pulsfire-mario&show_border=true"> -->

