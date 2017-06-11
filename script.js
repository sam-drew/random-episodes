var episodes = [
    [1,
        [80002472, 70295767, 70295768, 70295769, 70295770, 70295771, 70295772,
        70295773, 70295774, 70295775, 70295776, 70295777, 70295778, 70295779,
        70295780, 70295781, 70295782,]
    ],
    [2,
        [70295783, 70295784, 70295785, 70295786, 70295787, 70295788, 70295789,
        70295790, 70295791, 70295792, 70295793, 70295794, 70295795, 70295796,
        70295797, 70295798, 70295799, 70295800, 70295801, 70295802, 70295803,
        70295804, 70295805,]
    ]
];
window.onload=()=>{
    var season = episodes[Math.floor(Math.random() * episodes.length)][0];
    var episode = episodes[(season - 1)][1][Math.floor(Math.random() * episodes[(season - 1)][1].length)];
    var episode = episode.toString();
    var season = season.toString();
    var link = document.getElementById('link');
    link.href = 'http://www.netflix.com/watch/' + episode;
    document.getElementById("link").innerHTML = 'Season ' + season;
};
