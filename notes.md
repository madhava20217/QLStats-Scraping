
# Notes

## acceptcookie function

```
function acceptCookiePolicy() {
  setCookie("allowCookies", "true", true);

  var search = window.location.search;
  var params = {};
  search.replace(/[?&]+([^=&]+)=([^&]*)/gi, function(str,key,value) {
    params[key] = decodeURIComponent(value);
  });

  location.href = params["referer"] || "/";
}

setCookie("test", "ok", false);
if (getCookie("test") == "ok")
  setCookie("test", null);
else {
  document.getElementById("accept").style.display="none";
  document.getElementById("blocked").style.display="block";
}
```

## cookie info

```
QLStats
Leaderboard
News/Forum
Players
Games
Servers
Maps
Login/Sign-up
Cookie Policy
qlstats.net relies on the use of cookies to work properly.
qlstats itself uses cookies to remember your user preferences (game type, region, weapons in the accuracy graph, ...) and if you log in using your steam-id, a session-id.
3rd party components from Google and Valve/Steam, which are used by qlstats, may also set cookies, which can be used by these 3rd parties to track your browsing behavior across multiple sites.
To continue using qlstats, you need to agree to the use of cookies.
Agree
QLStats was created by PredatH0r as a Quake Live modification of XonStat, the Xonotic stats tracking system created by Antibody.
Both are licensed under GPLv2 and available on Github: QLStats, XonStat
Geo-IP information provided by freegeoip.net | Flag images provided by icondrawer.com
Legal information (contact, cookie policy, data privacy, disclaimer)
```