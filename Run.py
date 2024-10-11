import re, json, time, random, urllib.parse, os, requests, sys, webbrowser
from rich.console import Console
from rich.panel import Panel
from rich import print as printf
from requests.exceptions import RequestException


class fmt:

    def Println(self, string: str, end: str):
        printf(string, end=f"{end}")

    def Print(self, string: str):
        printf(string)

    def Scan(self, prompt: str):
        return Console().input(prompt)


LINK, COOKIES, LOOPING = (
    [],
    {
        'Cookie': 'null'
    },
    0,
)
fmt = fmt()


def Tampilkan_Banner():
    os.system("cls" if os.name == "nt" else "clear")
    fmt.Print(
        Panel(
            r"""[bold red]  _____ _    _____                                 
 |_   _| |  /  ___|                                
   | | | | _\ `--.  ___ __ _ _ __  _ __   ___ _ __ 
   | | | |/ /`--. \/ __/ _` | '_ \| '_ \ / _ \ '__|
   | | |   </\__/ / (_| (_| | | | | | | |  __/ |   
[bold white]   \_/ |_|\_\____/ \___\__,_|_| |_|_| |_|\___|_|   
             [underline green]Threads Dana Kaget Scanner""",
            width=56,
            style="bold bright_black",
        )
    )


def N_Threads_Scanner(cookies: str, query: str, visit: bool, delay: int):
    global LOOPING
    with requests.Session() as session:
        session.headers.update(
            {
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                "Upgrade-Insecure-Requests": "1",
                "Sec-Fetch-Mode": "navigate",
                "Host": "www.threads.net",
                "Sec-Fetch-Site": "none",
                "Accept-Language": "en-US,en;q=0.9",
                "Connection": "keep-alive",
                "Sec-Fetch-User": "?1",
                "Sec-Fetch-Dest": "document",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
            }  # Simulasikan "User-Agent" Agar Mendapatkan Hasil Yang Berbeda!
        )
        response = session.get(
            "https://www.threads.net/search/", verify=True, allow_redirects=True
        )

        try:
            jazoest = re.search(r'&jazoest=(\d+)"', response.text).group(1)
            __hsi = re.search(r'"hsi":"(\d+)"', response.text).group(1)
            lsd = re.search(r'\["LSD",\[\],{"token":"([^"]+)"}', response.text).group(1)
            __hs = re.search(r'"haste_session":"([^"]+)"', response.text).group(1)
            csrftoken = session.cookies.get_dict()["csrftoken"]
        except (AttributeError, KeyError):
            fmt.Print(
                Panel(
                    "[bold red]Sorry, Could not find the required data, you can try using Threads cookies!",
                    width=56,
                    style="bold bright_black",
                    title="[bold bright_black]> [Error] <",
                    title_align="center",
                )
            )
            sys.exit()
        ig_did_match = re.search(r'"device_id":"(.*?)"', response.text)
        ig_did = ig_did_match.group(1) if ig_did_match else ""
        mid_match = re.search(r'"machine_id":"(.*?)"', response.text)
        mid = mid_match.group(1) if mid_match else ""

        data = {
            "variables": '{"meta_place_id":null,"pinned_ids":null,"query":"'
            + str(query)
            + '","recent":1,"search_surface":"default","tagID":null,"__relay_internal__pv__BarcelonaIsLoggedInrelayprovider":false,"__relay_internal__pv__BarcelonaIsInlineReelsEnabledrelayprovider":true,"__relay_internal__pv__BarcelonaOptionalCookiesEnabledrelayprovider":true,"__relay_internal__pv__BarcelonaShowReshareCountrelayprovider":true,"__relay_internal__pv__BarcelonaQuotedPostUFIEnabledrelayprovider":false,"__relay_internal__pv__BarcelonaShouldShowFediverseM075Featuresrelayprovider":false}',
            "__comet_req": f"{random.randint(20, 30)}",
            "doc_id": "8051513244976314",
            "jazoest": f"{jazoest}",
            "__hs": f"{__hs}",
            "server_timestamps": "true",
            "lsd": f"{lsd}",
            "fb_api_caller_class": "RelayModern",
            "__hsi": f"{__hsi}",
            "fb_api_req_friendly_name": "BarcelonaSearchResultsQuery",
        }

        session.headers.update(
            {
                "Referer": "https://www.threads.net/search?q={}&serp_type=default".format(
                    urllib.parse.quote(query)
                ),
                "Origin": "https://www.threads.net",
                "Content-Type": "application/x-www-form-urlencoded",
                "X-IG-App-ID": "238260118697367",
                "Sec-Fetch-Site": "same-origin",
                "Sec-Fetch-Mode": "cors",
                "X-CSRFToken": "{}".format(csrftoken),
                "Accept": "*/*",
                "Sec-Fetch-Dest": "empty",
                "X-FB-LSD": "{}".format(lsd),
                "X-ASBD-ID": "129477",
                "Cookie": "csrftoken={}; dpr=1.5; mid={}; ig_did={}".format(
                    csrftoken, mid, ig_did
                ),
                "Content-Length": "{}".format(len(str(data))),
                "X-FB-Friendly-Name": "BarcelonaSearchResultsQuery",
            }
        )

        response2 = session.post(
            "https://www.threads.net/api/graphql",
            data=data,
            verify=True,
            allow_redirects=False,
        )
        if '"searchResults":' in response2.text:
            find_data = re.findall(r"kaget\?c=(.*?)&", str(json.loads(response2.text)))
            fmt.Println(
                "[bold bright_black]   ──>[bold green] %d Tautan Berhasil Ditemukan!          "
                % len(find_data),
                end="\r",
            )
            time.sleep(1.5)
            for code in find_data:
                done_link = open("Penyimpanan/Done.txt", "r+").read().splitlines()
                true_link = f"https://link.dana.id/kaget?c={code}"
                if str(true_link) in LINK or str(true_link) in done_link:
                    continue
                else:
                    LOOPING += 1
                    fmt.Print(
                        Panel(
                            "[bold green]%d[bold white]. Link:[bold red] %s."
                            % (LOOPING, true_link),
                            width=56,
                            style="bold bright_black",
                            title="[bold bright_black]> [Sukses] <",
                            title_align="center",
                        )
                    )
                    LINK.append("{}".format(true_link))
                    fmt.Println(
                        "[bold bright_black]   ──>[bold white] Menemukan:[bold green] link.dana.id/kaget?c=%s[bold white]!     "
                        % code,
                        end="\r",
                    )
                    time.sleep(0.5)
                    if visit == True:
                        (
                            webbrowser.open(url=true_link)
                            if os.name == "nt"
                            else os.system(f"xdg-open {true_link}")
                        )
                        for sleep in range(int(delay), 0, -1):
                            fmt.Println(
                                "[bold bright_black]   ──>[bold white] Tunggu[bold green] %d[bold white] Detik!                          "
                                % sleep,
                                end="\r",
                            )
                            time.sleep(1)
                        with open("Penyimpanan/Done.txt", "a+") as w:
                            w.write(f"{true_link}\n")
                        w.close()
                    continue
            fmt.Println(
                "[bold bright_black]   ──>[bold green] Selesai Mengumpulkan Tautan!               ",
                end="\r",
            )
            time.sleep(3.5)
            return True
        else:
            fmt.Println(
                "[bold bright_black]   ──>[bold red] Tautan Tidak Ditemukan!            ",
                end="\r",
            )
            time.sleep(5.0)
            return False


def L_Threads_Scanner(
    cookies: str, query: str, end_cursor: bool, visit: bool, delay: int
):
    global LOOPING
    with requests.Session() as session:
        session.headers.update(
            {
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                "Upgrade-Insecure-Requests": "1",
                "Sec-Fetch-Mode": "navigate",
                "Host": "www.threads.net",
                "Sec-Fetch-Site": "none",
                "Accept-Language": "en-US,en;q=0.9",
                "Connection": "keep-alive",
                "Sec-Fetch-User": "?1",
                "Sec-Fetch-Dest": "document",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
            }
        )
        response = session.get(
            "https://www.threads.net/search/",
            cookies={"Cookie": "{}".format(cookies)},
            verify=True,
            allow_redirects=True,
        )

        try:
            fb_dtsg = re.search(
                r'\["DTSGInitialData",\[\],{"token":"(.*?)"}', response.text
            ).group(1)
            lsd = re.search(r'\["LSD",\[\],{"token":"([^"]+)"}', response.text).group(1)
            __hs = re.search(r'"haste_session":"([^"]+)"', response.text).group(1)
            jazoest = re.search(r'&jazoest=(\d+)"', response.text).group(1)
            __hsi = re.search(r'"hsi":"(\d+)"', response.text).group(1)
        except AttributeError:
            fmt.Print(
                Panel(
                    "[bold red]Sorry, Could not find the required data. Your cooki\nes may not be working anymore!",
                    width=56,
                    style="bold bright_black",
                    title="[bold bright_black]> [Error] <",
                    title_align="center",
                )
            )
            sys.exit()
        data = f"av=&__user=0&__a=1&__req=y&__hs={urllib.parse.quote(__hs)}&dpr=1&__ccg=UNKNOWN&__rev=&__s=&__hsi={__hsi}&__dyn=&__csr=&__comet_req=29&fb_dtsg={urllib.parse.quote(fb_dtsg)}&jazoest={jazoest}&lsd={urllib.parse.quote(lsd)}&__spin_r=&__spin_b=trunk&__spin_t=&fb_api_caller_class=RelayModern&fb_api_req_friendly_name=BarcelonaSearchResultsQuery&variables=%7B%22meta_place_id%22%3Anull%2C%22pinned_ids%22%3Anull%2C%22query%22%3A%22{urllib.parse.quote(query)}%22%2C%22recent%22%3A1%2C%22search_surface%22%3A%22default%22%2C%22tagID%22%3Anull%2C%22__relay_internal__pv__BarcelonaIsLoggedInrelayprovider%22%3Atrue%2C%22__relay_internal__pv__BarcelonaIsInlineReelsEnabledrelayprovider%22%3Atrue%2C%22__relay_internal__pv__BarcelonaOptionalCookiesEnabledrelayprovider%22%3Atrue%2C%22__relay_internal__pv__BarcelonaShowReshareCountrelayprovider%22%3Atrue%2C%22__relay_internal__pv__BarcelonaQuotedPostUFIEnabledrelayprovider%22%3Afalse%2C%22__relay_internal__pv__BarcelonaIsCrawlerrelayprovider%22%3Afalse%2C%22__relay_internal__pv__BarcelonaShouldShowFediverseM075Featuresrelayprovider%22%3Afalse%7D&server_timestamps=true&doc_id=8447423912005204"

        session.headers.update(
            {
                "Referer": "https://www.threads.net/search?q={}&serp_type=default".format(
                    urllib.parse.quote(query)
                ),
                "Origin": "https://www.threads.net",
                "Content-Type": "application/x-www-form-urlencoded",
                "X-IG-App-ID": "238260118697367",
                "Sec-Fetch-Site": "same-origin",
                "Sec-Fetch-Mode": "cors",
                "X-CSRFToken": "{}".format(
                    re.search("csrftoken=(.*?);", str(cookies)).group(1)
                ),
                "Accept": "*/*",
                "Sec-Fetch-Dest": "empty",
                "X-FB-LSD": "{}".format(lsd),
                "X-ASBD-ID": "129477",
                "Content-Length": "{}".format(len(str(data))),
                "X-FB-Friendly-Name": "BarcelonaSearchResultsQuery",
            }
        )
        response2 = session.post(
            "https://www.threads.net/api/graphql",
            data=data,
            cookies={"Cookie": "{}".format(cookies)},
            verify=True,
            allow_redirects=False,
        )
        if '"searchResults":' in response2.text:
            json_response = json.loads(response2.text)
            find_data = re.findall(r"kaget\?c=(.*?)&", str(json_response))
            fmt.Println(
                "[bold bright_black]   ──>[bold green] %d Tautan Berhasil Ditemukan!          "
                % len(find_data),
                end="\r",
            )
            time.sleep(1.5)
            for code in find_data:
                done_link = open("Penyimpanan/Done.txt", "r+").read().splitlines()
                true_link = f"https://link.dana.id/kaget?c={code}"
                if str(true_link) in LINK or str(true_link) in done_link:
                    continue
                else:
                    LOOPING += 1
                    fmt.Print(
                        Panel(
                            "[bold green]%d[bold white]. Link:[bold red] %s."
                            % (LOOPING, true_link),
                            width=56,
                            style="bold bright_black",
                            title="[bold bright_black]> [Sukses] <",
                            title_align="center",
                        )
                    )
                    LINK.append("{}".format(true_link))
                    fmt.Println(
                        "[bold bright_black]   ──>[bold white] Menemukan:[bold green] link.dana.id/kaget?c=%s[bold white]!     "
                        % code,
                        end="\r",
                    )
                    time.sleep(0.5)

                    if visit == True:
                        (
                            webbrowser.open(url=true_link)
                            if os.name == "nt"
                            else os.system(f"xdg-open {true_link}")
                        )
                        for sleep in range(int(delay), 0, -1):
                            fmt.Println(
                                "[bold bright_black]   ──>[bold white] Tunggu[bold green] %d[bold white] Detik!                          "
                                % sleep,
                                end="\r",
                            )
                            time.sleep(1)
                        with open("Penyimpanan/Done.txt", "a+") as w:
                            w.write(f"{true_link}\n")
                        w.close()
                    continue
            has_next_page = bool(
                json_response["data"]["searchResults"]["page_info"]["has_next_page"]
            )
            if end_cursor == True and has_next_page == True:
                after = json_response["data"]["searchResults"]["page_info"][
                    "end_cursor"
                ]
                fmt.Println(
                    "[bold bright_black]   ──>[bold green] Berhasil Menemukan Next Cursor!         ",
                    end="\r",
                )
                time.sleep(3.5)

                Next_Threads_Finder(
                    session=session,
                    cookies=cookies,
                    query=query,
                    fb_dtsg=fb_dtsg,
                    lsd=lsd,
                    __hs=__hs,
                    jazoest=jazoest,
                    __hsi=__hsi,
                    after=after,
                    visit=visit,
                    delay=delay,
                )
            else:
                fmt.Println(
                    "[bold bright_black]   ──>[bold red] Tidak Menemukan Next Cursor!            ",
                    end="\r",
                )
                time.sleep(3.5)
                return True
        else:
            fmt.Println(
                "[bold bright_black]   ──>[bold red] Tautan Tidak Ditemukan!            ",
                end="\r",
            )
            time.sleep(5.0)
            return False


def Next_Threads_Finder(
    session: str,
    cookies: str,
    query: str,
    fb_dtsg: str,
    lsd: str,
    __hs: str,
    jazoest: int,
    __hsi: int,
    after: str,
    visit: bool,
    delay: int,
):
    global LOOPING
    data = f"av=&__user=0&__a=1&__req=18&__hs{urllib.parse.quote(__hs)}=&dpr=1&__ccg=UNKNOWN&__rev=&__s=&__hsi={__hsi}&__dyn=&__csr=&__comet_req=29&fb_dtsg={urllib.parse.quote(fb_dtsg)}&jazoest={jazoest}&lsd={urllib.parse.quote(lsd)}&__spin_r=&__spin_b=trunk&__spin_t=&fb_api_caller_class=RelayModern&fb_api_req_friendly_name=BarcelonaSearchResultsRefetchableQuery&variables=%7B%22after%22%3A%22{urllib.parse.quote(after)}%22%2C%22before%22%3Anull%2C%22first%22%3A10%2C%22last%22%3Anull%2C%22meta_place_id%22%3Anull%2C%22pinned_ids%22%3Anull%2C%22query%22%3A%22{query}%22%2C%22recent%22%3A1%2C%22search_surface%22%3A%22default%22%2C%22tagID%22%3Anull%2C%22__relay_internal__pv__BarcelonaIsLoggedInrelayprovider%22%3Atrue%2C%22__relay_internal__pv__BarcelonaIsInlineReelsEnabledrelayprovider%22%3Atrue%2C%22__relay_internal__pv__BarcelonaOptionalCookiesEnabledrelayprovider%22%3Atrue%2C%22__relay_internal__pv__BarcelonaShowReshareCountrelayprovider%22%3Atrue%2C%22__relay_internal__pv__BarcelonaQuotedPostUFIEnabledrelayprovider%22%3Afalse%2C%22__relay_internal__pv__BarcelonaIsCrawlerrelayprovider%22%3Afalse%2C%22__relay_internal__pv__BarcelonaShouldShowFediverseM075Featuresrelayprovider%22%3Afalse%7D&server_timestamps=true&doc_id=26899752706339177"
    session.headers.update(
        {
            "X-FB-Friendly-Name": "BarcelonaSearchResultsRefetchableQuery",
            "Content-Length": "{}".format(len(str(data))),
            "Referer": "https://www.threads.net/search?q={}&serp_type=default&filter=recent".format(
                query
            ),
        }
    )
    response3 = session.post(
        "https://www.threads.net/api/graphql",
        data=data,
        cookies={"Cookie": "{}".format(cookies)},
        verify=True,
        allow_redirects=False,
    )
    if '"searchResults":' in response3.text:
        json_response = json.loads(response3.text)
        find_data = re.findall(r"kaget\?c=(.*?)&", str(json_response))
        fmt.Println(
            "[bold bright_black]   ──>[bold green] %d Tautan Berhasil Ditemukan!          "
            % len(find_data),
            end="\r",
        )
        time.sleep(1.5)
        for code in find_data:
            done_link = open("Penyimpanan/Done.txt", "r+").read().splitlines()
            true_link = f"https://link.dana.id/kaget?c={code}"
            if str(true_link) in LINK or str(true_link) in done_link:
                continue
            else:
                LOOPING += 1
                fmt.Print(
                    Panel(
                        "[bold green]%d[bold white]. Link:[bold red] %s."
                        % (LOOPING, true_link),
                        width=56,
                        style="bold bright_black",
                        title="[bold bright_black]> [Sukses] <",
                        title_align="center",
                    )
                )
                LINK.append("{}".format(true_link))
                fmt.Println(
                    "[bold bright_black]   ──>[bold white] Menemukan:[bold green] link.dana.id/kaget?c=%s[bold white]!     "
                    % code,
                    end="\r",
                )
                time.sleep(0.5)

                if visit == True:
                    (
                        webbrowser.open(url=true_link)
                        if os.name == "nt"
                        else os.system(f"xdg-open {true_link}")
                    )
                    for sleep in range(int(delay), 0, -1):
                        fmt.Println(
                            "[bold bright_black]   ──>[bold white] Tunggu[bold green] %d[bold white] Detik!                          "
                            % sleep,
                            end="\r",
                        )
                        time.sleep(1)
                    with open("Penyimpanan/Done.txt", "a+") as w:
                        w.write(f"{true_link}\n")
                    w.close()
                continue
        has_next_page = bool(
            json_response["data"]["searchResults"]["page_info"]["has_next_page"]
        )
        if has_next_page == True:
            after = json_response["data"]["searchResults"]["page_info"]["end_cursor"]
            fmt.Println(
                "[bold bright_black]   ──>[bold green] Berhasil Menemukan Next Cursor!         ",
                end="\r",
            )
            time.sleep(3.5)

            Next_Threads_Finder(
                session=session,
                cookies=cookies,
                query=query,
                fb_dtsg=fb_dtsg,
                lsd=lsd,
                __hs=__hs,
                jazoest=jazoest,
                __hsi=__hsi,
                after=after,
                visit=visit,
                delay=delay,
            )
        else:
            fmt.Println(
                "[bold bright_black]   ──>[bold red] Tidak Menemukan Next Cursor!            ",
                end="\r",
            )
            time.sleep(3.5)
            return True
    else:
        fmt.Println(
            "[bold bright_black]   ──>[bold red] Tautan Tidak Ditemukan!            ",
            end="\r",
        )
        time.sleep(5.0)
        return False


if __name__ == "__main__":
    Tampilkan_Banner()

    if os.path.exists("Penyimpanan/Done.txt") == False:
        open("Penyimpanan/Done.txt", "w").close()
    Stop = False
    while Stop == False:
        fmt.Print(
            Panel(
                "[bold white]Please fill in the query or search keyword, you can type `[bold red]LIST[bold white]` to display the keyword, for examp\nle:[bold green] link dana id[bold white] *[bold red]Remember to only enter one query[bold white]!",
                width=56,
                style="bold bright_black",
                title="[bold bright_black]> [Pertanyaan] <",
                title_align="center",
                subtitle="[bold bright_black]╭─────",
                subtitle_align="left",
            )
        )
        query = fmt.Scan("[bold bright_black]   ╰─> ")
        if query.lower() == "list":
            fmt.Print(
                Panel(
                    "[bold white]List Keyword:[bold green] link dana id[bold white],[bold green]dana kaget[bold white],[bold green]dana id[bold white],[bold green]dana id kaget[bold white],[bold green]lagi sebar DANA[bold white]!",
                    width=56,
                    style="bold bright_black",
                    title="[bold bright_black]> [Query] <",
                    title_align="center",
                )
            )
            continue
        else:
            Stop = True
    fmt.Print(
        Panel(
            "[bold white]You want to open the dana application automatically, type[bold green] Y[bold white] if you want and type[bold red] N[bold white] if you don't!",
            width=56,
            style="bold bright_black",
            title="[bold bright_black]> [Pertanyaan] <",
            title_align="center",
            subtitle="[bold bright_black]╭─────",
            subtitle_align="left",
        )
    )
    opens = fmt.Scan("[bold bright_black]   ╰─> ")
    if opens.lower() != "y":
        visit = False
        delay = 60
    else:
        visit = True
        fmt.Print(
            Panel(
                "[bold white]Please fill in the delay to open the next link, we r\necommend 30 seconds. For\nexample:[bold green] 60 seconds[bold white] *[bold red]Remember to enter only numbers[bold white]!",
                width=56,
                style="bold bright_black",
                title="[bold bright_black]> [Delay] <",
                title_align="center",
                subtitle="[bold bright_black]╭─────",
                subtitle_align="left",
            )
        )
        delay = int(fmt.Scan("[bold bright_black]   ╰─> "))
    cookies = COOKIES["Cookie"]
    if "sessionid=" in str(cookies) and "csrftoken=" in str(cookies):
        fmt.Print(
            Panel(
                "[bold white]You want to get the link on one page only? If you want you can type[bold red] Y[bold white] if not type[bold green] N[bold white]!",
                width=56,
                style="bold bright_black",
                title="[bold bright_black]> [Halaman] <",
                title_align="center",
                subtitle="[bold bright_black]╭─────",
                subtitle_align="left",
            )
        )
        halaman = fmt.Scan("[bold bright_black]   ╰─> ")
        end_cursor = False if halaman.lower() == "y" else True
        fmt.Print(
            Panel(
                "[bold white]You can use[bold green] CTRL + C[bold white] if you want to reload and if you want to stop press[bold red] CTRL + Z[bold white]!",
                width=56,
                style="bold bright_black",
                title="[bold bright_black]> [Catatan] <",
                title_align="center",
            )
        )
        while True:
            try:
                fmt.Println(
                    "[bold bright_black]   ──>[bold green] Sedang Mencari Tautan!            ",
                    end="\r",
                )
                time.sleep(4.5)
                L_Threads_Scanner(
                    cookies=cookies,
                    query=query,
                    end_cursor=end_cursor,
                    visit=visit,
                    delay=delay,
                )
                time.sleep(60)
            except RequestException:
                fmt.Println(
                    "[bold bright_black]   ──>[bold yellow] RequestException!               ",
                    end="\r",
                )
                time.sleep(10.0)
                continue
            except KeyboardInterrupt:
                fmt.Println("           ", end="\r")
                time.sleep(2.5)
                continue
    else:
        fmt.Print(
            Panel(
                "[bold white]You can use[bold green] CTRL + C[bold white] if you want to reload and if you want to stop press[bold red] CTRL + Z[bold white]!",
                width=56,
                style="bold bright_black",
                title="[bold bright_black]> [Catatan] <",
                title_align="center",
            )
        )
        while True:
            try:
                fmt.Println(
                    "[bold bright_black]   ──>[bold green] Sedang Mencari Tautan!            ",
                    end="\r",
                )
                time.sleep(4.5)
                N_Threads_Scanner(cookies="null", query=query, visit=visit, delay=delay)
                time.sleep(60)
            except RequestException:
                fmt.Println(
                    "[bold bright_black]   ──>[bold yellow] RequestException!               ",
                    end="\r",
                )
                time.sleep(10.0)
                continue
            except KeyboardInterrupt:
                fmt.Println("           ", end="\r")
                time.sleep(2.5)
                continue