# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|
  config.vm.box = "ubuntu/trusty64"

  config.vm.define "full-text-search-django-mysql-vm" do |vm_define|
  end

  config.vm.hostname = "django-full-text-search-django.local"

  config.vm.network "forwarded_port", guest: 8000, host: 8000

  config.vm.synced_folder ".", "/home/vagrant/full_text_search_django/"

  config.vm.provider "virtualbox" do |vb|
    vb.memory = "1024"
    vb.name = "full-text-search-django-mysql-vm"
  end

  config.vm.provision "shell", inline: <<-SHELL
    export DEBIAN_FRONTEND=noninteractive

    apt-get update
    debconf-set-selections <<< 'mysql-server mysql-server/root_password password fts_django'
    debconf-set-selections <<< 'mysql-server mysql-server/root_password_again password fts_django'
    apt-get install -y python3 python3-dev python3.4-venv mysql-server-5.6 libmysqlclient-dev
    /usr/bin/mysql --user=root --password=fts_django --execute='CREATE DATABASE full_text_search_django;'
    /usr/bin/mysql --user=root --password=fts_django --execute="CREATE USER 'fts_django'@'localhost' IDENTIFIED BY 'fts_django';"
    /usr/bin/mysql --user=root --password=fts_django --execute="GRANT ALL ON full_text_search_django.* to 'fts_django'@'localhost';"
  SHELL

  config.vm.provision "shell", privileged: false, inline: <<-SHELL
    pyvenv-3.4 --without-pip full_text_search_django_venv
    source full_text_search_django_venv/bin/activate
    curl --silent --show-error --retry 5 https://bootstrap.pypa.io/get-pip.py | python

    pip install -r full_text_search_django/requirements.txt

    cd full_text_search_django/full_text_search_django/

    python manage.py migrate

    echo '
    [
        {
            "model": "items.Item",
            "pk": 1,
            "fields": {
                "name": "quis lectus. Nullam suscipit, est ac facilisis",
                "description": "ujVAdcI PCAUyrD tqUQTcdhsIv IrqHsnNLmCu elAVuHKPnD rhVsj byarJo sKIOok OmMkPcTS"
            }
        },
        {
            "model": "items.Item",
            "pk": 2,
            "fields": {
                "name": "pede, ultrices a, auctor non, feugiat",
                "description": "mjHJRpw agYoOULWmzNe gcQapotzjZqM"
            }
        },
        {
            "model": "items.Item",
            "pk": 3,
            "fields": {
                "name": "enim, condimentum eget, volutpat ornare, facilisis eget, ipsum. Donec sollicitudin",
                "description": "fuIiBOt GjpBUTa udFAGNCyO jiYZOFAlnz HIZfztuVrWxe iuqwAG"
            }
        },
        {
            "model": "items.Item",
            "pk": 4,
            "fields": {
                "name": "a, malesuada id, erat. Etiam vestibulum",
                "description": "frakVZY toJpGcIKxz vqnAzTuPNY tubYfjwmKRZO nOatpNsBQkM HZzStbj qObrFxahmN nsAHxiduc LKgvZ puXaW lFQyAsEW HfEKSGVOheNF EMcbN"
            }
        },
        {
            "model": "items.Item",
            "pk": 5,
            "fields": {
                "name": "conubia nostra, per",
                "description": "RetQ PoyDISegXhpA ncLSbUvrq aBXfneQ SXeMPBc dLIWtnSkYDiK esdrVCBznPY bdfVahLZUl TCoihmpqWJ lxhmSyq SlAM fOtDnj"
            }
        },
        {
            "model": "items.Item",
            "pk": 6,
            "fields": {
                "name": "tincidunt, nunc",
                "description": "uVSGLMrjidfR iNGzlCIA jEvaJKeuxn"
            }
        },
        {
            "model": "items.Item",
            "pk": 7,
            "fields": {
                "name": "aliquet. Proin velit.",
                "description": "TfWUkdiKaJ RCfSdJwA wuMvr wxDlaEn GFozXv"
            }
        },
        {
            "model": "items.Item",
            "pk": 8,
            "fields": {
                "name": "eget, volutpat ornare, facilisis",
                "description": "igdADlmqySv HsFMIaL OZjfi WsraMqwDElo PCxjsleSoXv jRYcxFSVI jfqtBYbTW WDfmbjnrF BbQWyYo nvArImHl PDVa agMuLFtfC rmcR HbcBahDk XNwgebJkd"
            }
        },
        {
            "model": "items.Item",
            "pk": 9,
            "fields": {
                "name": "sagittis.",
                "description": "HwYjpoIqxNM mpSVPJkWLuh lHsIFiax FOThYvlsn RBUmKN DsoO YSPxM dKOcW UkAbjKmWNOM"
            }
        },
        {
            "model": "items.Item",
            "pk": 10,
            "fields": {
                "name": "porttitor interdum.",
                "description": "juEdbo PIVdqSZkQFoY atlxyvFSGd HBWuTgS yxjon XiqgjuzEU AesLw"
            }
        },
        {
            "model": "items.Item",
            "pk": 11,
            "fields": {
                "name": "tincidunt aliquam arcu. Aliquam ultrices iaculis odio. Nam interdum enim",
                "description": "YMzWahXfojAr VMwTNQWdfHRq xBHFScwGzQn RgxtE"
            }
        },
        {
            "model": "items.Item",
            "pk": 12,
            "fields": {
                "name": "felis purus ac tellus.",
                "description": "sOFQN WlrzA warWl gpxVq xcaI xyfEobvnCP pLjReuoYtxs lwtDIbS eIHzohiuY lXETDpdO"
            }
        },
        {
            "model": "items.Item",
            "pk": 13,
            "fields": {
                "name": "ante blandit viverra. Donec tempus,",
                "description": "faoKx KEkyPQW vtMKyNoFg afZyPBGivT OdzNj IJZkhVoc EUdxILS IgDEifCt jWQxpB TUwFCSkns"
            }
        },
        {
            "model": "items.Item",
            "pk": 14,
            "fields": {
                "name": "non dui",
                "description": "unNRSHjCLb RIfahvGpkbs Itjz XKguJ nhXKmICuJHvj fZkTKQxMC VgTzJ ikmwFGLl oQUyWZKP nwjrhCf AvVFLTNeqi oVLe"
            }
        },
        {
            "model": "items.Item",
            "pk": 15,
            "fields": {
                "name": "Nullam feugiat placerat velit. Quisque varius.",
                "description": "MzCdqOmsKTLi vagWd gUBiOI bdemzO NVnWYq qrQikoyjS"
            }
        },
        {
            "model": "items.Item",
            "pk": 16,
            "fields": {
                "name": "Phasellus ornare.",
                "description": "Fvtir pPNQctq yCdXRFz CdyeRUtf FdXCZ JovWtNPF hUDIkAveX"
            }
        },
        {
            "model": "items.Item",
            "pk": 17,
            "fields": {
                "name": "luctus, ipsum leo elementum sem, vitae",
                "description": "vuTndHE VquSmnMoZl Mfhjxt wpiPFlyzU rSDtwosjMPi pijuGl AifMGzaqE CdLDqNKsF zRPlEubyLFBY plRJPOEKM DBeKdqCVF MpmN"
            }
        },
        {
            "model": "items.Item",
            "pk": 18,
            "fields": {
                "name": "facilisi. Sed",
                "description": "RAvHrnWK fUXuBds eWDT KRdpzlYO kbELuZsehKxn bzjli wYZltjF"
            }
        },
        {
            "model": "items.Item",
            "pk": 19,
            "fields": {
                "name": "Curabitur ut",
                "description": "kmvXCJEzSF HEpXMdC EUmCSh rykUnKV wqDPijs VjlvFpHMIy AyrXiZjntFS SZONerz OmKoxJRFUr OxoVXI BWJal FjxOPMDJUXw DqFcBGH hUydpCTFeit"
            }
        },
        {
            "model": "items.Item",
            "pk": 20,
            "fields": {
                "name": "a odio semper cursus. Integer",
                "description": "dyNWbgjkOZF YHoTmc VKPUZeNkF WTzUOCtkG NoIbwFWGJ"
            }
        },
        {
            "model": "items.Item",
            "pk": 21,
            "fields": {
                "name": "dis parturient montes, nascetur ridiculus mus. Proin vel nisl.",
                "description": "FUfbYVCeNP bIrq dpGjWeSQxnNy tziwpDynUvC NexvOXS bxkvizqO CpsISeJ NmyesUp QHcvkRWjrlwJ ajhpHJ lJumMVR JibqwW KgShAxqV"
            }
        },
        {
            "model": "items.Item",
            "pk": 22,
            "fields": {
                "name": "elit, dictum eu, eleifend nec, malesuada ut, sem.",
                "description": "jikXNAxvdU OdRxiBGrJe JNxwWLEXpt"
            }
        },
        {
            "model": "items.Item",
            "pk": 23,
            "fields": {
                "name": "In ornare sagittis felis.",
                "description": "gFXL LglZFCtOaPv RjdcUtS FlRMOBzDv OjRkfAt SNZs"
            }
        },
        {
            "model": "items.Item",
            "pk": 24,
            "fields": {
                "name": "nisi.",
                "description": "xITmCEe xGqKmjn kUsDJHjRlMV XPWN HBAwiVLv CDvezBfS FBswtShCGolY sFfcXTWpbh pELIPbnXoKwB DzGIXTUSseZ"
            }
        },
        {
            "model": "items.Item",
            "pk": 25,
            "fields": {
                "name": "est ac mattis semper, dui lectus rutrum",
                "description": "sJvHRuUnK cuHTKGO sdFjykID JGXsIzgunQ oQWb pWfLBY pfcYrktTAxy HwgNOlCf HjhQMbe juAlGXHD zTghwQlomNaO kyCWncOHYd YiTGnwAjk ISaUCm RoMOhs"
            }
        },
        {
            "model": "items.Item",
            "pk": 26,
            "fields": {
                "name": "dolor dapibus gravida. Aliquam",
                "description": "MUfdIGn zFpEoVMjdf zqSrBlhLauAe ufJVXFU tORuHeZl FTsiL ecFaAmUvYEg OhzefBg PCxbqpRhjtg YMvADkq wLCYqsyAMX ncvS zPZGK XycPaHro zjTcXCSqhLE"
            }
        },
        {
            "model": "items.Item",
            "pk": 27,
            "fields": {
                "name": "arcu. Curabitur ut odio vel est tempor",
                "description": "CulYhFLrfbU OfFm SeLfNkn GubrKX yniaNv lsLTFjOJqR tguAVfJbs Nijposax tziMsKuAQ FNeX xspX bkDFnPaZ"
            }
        },
        {
            "model": "items.Item",
            "pk": 28,
            "fields": {
                "name": "Sed",
                "description": "hyoUdTI HndirI POUveLz IkdCUyL kbilvuLp VUrPtkJ GpzXIDOKkci bUqr QkosH zLWMJtP RIjTB KvqXl zaIHkn LFpIW"
            }
        },
        {
            "model": "items.Item",
            "pk": 29,
            "fields": {
                "name": "lectus rutrum urna, nec luctus felis purus ac",
                "description": "vSWUZJbmtHdq qAxRoMkKmC jBpWMSdiFhUN fxvuP eWTO wstlOLk ZaXbqBT tTMg dlcjWtAoTH WNeqFHQU iFmgGWoc rhKLGquWQMHD hVAXdqJPHNsK"
            }
        },
        {
            "model": "items.Item",
            "pk": 30,
            "fields": {
                "name": "sagittis. Duis gravida. Praesent eu nulla",
                "description": "ixkUaIwnETOJ OTGmXzuNJ NtjWEuYHRwB VNXnhmKB zZQRqvGHw uperIjS kurQD JfMXHc YWvL ltgLhvBuK HZIVhtbAsJ"
            }
        },
        {
            "model": "items.Item",
            "pk": 31,
            "fields": {
                "name": "enim. Etiam imperdiet dictum magna. Ut tincidunt orci quis lectus.",
                "description": "gCIulVTorF DTNchjpBefra cERSXg uGhW AjlNzrT ITUK lEoJZrGRa nuhpDBgFm WDQkn tXpIKCcJl AJUt"
            }
        },
        {
            "model": "items.Item",
            "pk": 32,
            "fields": {
                "name": "vestibulum nec, euismod in, dolor. Fusce",
                "description": "DeksNmah bOwhKSP LNgtJwC heLVngEqyx VlCMPwmKkGfz QxkVWhil SGdquonE jpSJKZqXB uIrPefcTLpB HCYpBvLA vuWDtrPn VHxsCFqnTIpS oIsXdgzHBF KWXjyJ"
            }
        },
        {
            "model": "items.Item",
            "pk": 33,
            "fields": {
                "name": "blandit. Nam nulla magna, malesuada vel, convallis",
                "description": "NcvASraBDK nqaUJ DAvWzq GZJdLqvhnT uyUsEgLv jtKpHY oRYdx hETBVRclDQ FJgCpsWVYOb hdabYEfps"
            }
        },
        {
            "model": "items.Item",
            "pk": 34,
            "fields": {
                "name": "Morbi sit amet massa. Quisque porttitor eros nec",
                "description": "XVtOY DLqsUlrCQ NVUsg"
            }
        },
        {
            "model": "items.Item",
            "pk": 35,
            "fields": {
                "name": "placerat. Cras dictum",
                "description": "dCBiYbwSv sJDzVMkwmxoP XzlFWbqxei HbxyznlXNVS wlrzPOU hzPVqaWQgJl evFX EwsjcrbNUSV nmcTJAeyp ZNcgORjfmx"
            }
        },
        {
            "model": "items.Item",
            "pk": 36,
            "fields": {
                "name": "tortor nibh sit amet orci. Ut sagittis",
                "description": "aYhDwj fTHqhF gUsSrlMXy gWQHAJyc lVgstbRpjcTX wGkgC NrhIanPJAkgK obfFdvGQtpjZ DTbHwYdemkaQ wzAcj UjmaVhK"
            }
        },
        {
            "model": "items.Item",
            "pk": 37,
            "fields": {
                "name": "velit.",
                "description": "nViEYMKbJNu EJIblUR tCHwrfdpTi bKBkcTlM"
            }
        },
        {
            "model": "items.Item",
            "pk": 38,
            "fields": {
                "name": "nec urna suscipit nonummy. Fusce fermentum fermentum arcu.",
                "description": "zsxGdBRgl brjGt wyVpAfC CcWy roZafLtAPj"
            }
        },
        {
            "model": "items.Item",
            "pk": 39,
            "fields": {
                "name": "arcu. Vestibulum ante",
                "description": "iJTDdfe wjkVvFH asnzXkFvycE nSwTzAqYR QmPbdlcZ dDRCh EHZUxylI"
            }
        },
        {
            "model": "items.Item",
            "pk": 40,
            "fields": {
                "name": "Morbi sit amet massa. Quisque porttitor eros",
                "description": "aSscHTZFnKUW JkIBiVl HbXWJT MiURIAfye txOZQCUPNo iBSjLCslR AsdONo tmUiRShj qykZfsh xPTyG RiqlIxnY"
            }
        },
        {
            "model": "items.Item",
            "pk": 41,
            "fields": {
                "name": "gravida",
                "description": "sUihpSQMNRer TkOYbyCPLf IFVRJ dhlHp"
            }
        },
        {
            "model": "items.Item",
            "pk": 42,
            "fields": {
                "name": "et magnis dis parturient montes, nascetur ridiculus mus. Aenean eget",
                "description": "gXyAS GfRPTWaIL cpGvnjOyYRKT GSPzHXwjyaLJ lwYHKsBROxPz dDonKLAM gLkp LkjeafXgPq FqHc aPVE IMUYSBOlZk"
            }
        },
        {
            "model": "items.Item",
            "pk": 43,
            "fields": {
                "name": "diam. Pellentesque habitant morbi tristique senectus",
                "description": "FHxNiRJhZb IzWxAnCeY pXJOT"
            }
        },
        {
            "model": "items.Item",
            "pk": 44,
            "fields": {
                "name": "Nunc quis arcu vel quam dignissim pharetra. Nam ac",
                "description": "dlcfFnJ gfxRIPeZQT uQapJSYHPX YOfpBE inRcrs LBVuOpq IPksod ynai DPwIjqVtiLR CTRxGOpy aftGOZg eiowyF KHcJsgFE AMNn eNmsJa"
            }
        },
        {
            "model": "items.Item",
            "pk": 45,
            "fields": {
                "name": "at, velit. Cras lorem lorem, luctus ut, pellentesque eget,",
                "description": "saqthnDyY kLGlVTbDCP sIzRbliutWOC NLHez tWwzvJcOPK VjkDdG ANJOhL"
            }
        },
        {
            "model": "items.Item",
            "pk": 46,
            "fields": {
                "name": "Fusce aliquet magna",
                "description": "gnQicPBuJyUE wZPaQmRHDY Mkep"
            }
        },
        {
            "model": "items.Item",
            "pk": 47,
            "fields": {
                "name": "Aliquam vulputate ullamcorper magna. Sed eu",
                "description": "tVqQBgdEO FCQt PtJilOLTgCk HEjIfJukATMw dIGfNK YZxVlzHDAcEq rkAeYUVuiHTc BbdZ wlbRoZn vDyQtcjNVken tjQZ KnaeIuXdM IjYNlLZ MgicFHAI PfuvawZUAC"
            }
        },
        {
            "model": "items.Item",
            "pk": 48,
            "fields": {
                "name": "mattis. Integer eu",
                "description": "HathvpBmWQ LORup kDaqXx"
            }
        },
        {
            "model": "items.Item",
            "pk": 49,
            "fields": {
                "name": "nec tellus. Nunc lectus pede,",
                "description": "DqwpJa PDZnvjLRJa WOHmkidRz jhIpu"
            }
        },
        {
            "model": "items.Item",
            "pk": 50,
            "fields": {
                "name": "sapien. Cras dolor dolor, tempus non, lacinia at, iaculis",
                "description": "ivaefHNwOyA oFeqxNVsIB HLUsrdOFfT rIdPfajqQc NDfveTkPXlY LbinrkqSOgs"
            }
        },
        {
            "model": "items.Item",
            "pk": 51,
            "fields": {
                "name": "erat, in consectetuer ipsum nunc id",
                "description": "SDExZnRqNY hSTvqJLFlpAB JlyRDQAjt koqAZtuX tKJekfPRcnL JQWwNkKGS rHSCZ skRy JoNvdLEYD ObTc"
            }
        },
        {
            "model": "items.Item",
            "pk": 52,
            "fields": {
                "name": "mauris. Suspendisse aliquet molestie",
                "description": "MNBULqf ItSV jMZcBhE jqgCQFMX yLUwqzQjXb iMEKmSFsf hjrSmb"
            }
        },
        {
            "model": "items.Item",
            "pk": 53,
            "fields": {
                "name": "aliquet diam. Sed diam",
                "description": "GajxlsTwhr kpygxjAeZ OnRwHFNvQW BJLdnetlfp MbSIFvxr"
            }
        },
        {
            "model": "items.Item",
            "pk": 54,
            "fields": {
                "name": "adipiscing elit. Aliquam auctor,",
                "description": "cyAbiYTNzLq XYJH KgYXw KaoU BzbFwkshUJ"
            }
        },
        {
            "model": "items.Item",
            "pk": 55,
            "fields": {
                "name": "erat.",
                "description": "NpyYJnXPAcU GKSJpPHimle vYNyRuEKhrf djNrKx pjoIsyh NiOPLKaRB MqvTJtdBI vIgAYl"
            }
        },
        {
            "model": "items.Item",
            "pk": 56,
            "fields": {
                "name": "eleifend,",
                "description": "ZrBVhe SxMzDGoZRyeY nKIseYiXFmQ uawBt bdMxCyNqgr YUDnzco hOrDzEMSPij WmHZi MgUcDOSuw YhblANFM aJUmYdojBQFq qxgEae"
            }
        },
        {
            "model": "items.Item",
            "pk": 57,
            "fields": {
                "name": "ultrices sit amet, risus. Donec nibh enim, gravida sit amet,",
                "description": "HuSoTI IpGecqlVjX XzkRynq PXCm"
            }
        },
        {
            "model": "items.Item",
            "pk": 58,
            "fields": {
                "name": "quis urna. Nunc quis arcu vel quam dignissim",
                "description": "YmVHobBIM HOQWPNnMbGe SbkJn"
            }
        },
        {
            "model": "items.Item",
            "pk": 59,
            "fields": {
                "name": "rutrum. Fusce dolor quam, elementum",
                "description": "sagPj hoNrmjtYw XbpIJLhlsV"
            }
        },
        {
            "model": "items.Item",
            "pk": 60,
            "fields": {
                "name": "erat eget ipsum. Suspendisse sagittis. Nullam vitae diam.",
                "description": "NTGOstzM WdRFkUEBbgjp YCqpuAroB aDAVbthCg OQMXaiCyPNVW IlOCkX BCKJbhTyXYeP wWPT puqHGOEyXCkl VuyHzi vAEGTWJys rChUa WQlEF CRGUIzLFaptm iEIaXPUTKFbe"
            }
        },
        {
            "model": "items.Item",
            "pk": 61,
            "fields": {
                "name": "nec ante. Maecenas mi",
                "description": "evVTAyJF xzMJ JhSel xnzFJN pMHL vdrb LyUvMrcJZgRN DczihFXgStOC kqcYbzr hcUOftNqj"
            }
        },
        {
            "model": "items.Item",
            "pk": 62,
            "fields": {
                "name": "tincidunt, neque",
                "description": "fSeyokjCDHQ XZatEj qjEH whca wvqe VzkcdHej ZvaDTuxnW jOhCfg bvNBM brEQjPzgGiyZ TLlRFu NXyTxAlWk YdEJFyO DGTrWQxVhn vGopLDf"
            }
        },
        {
            "model": "items.Item",
            "pk": 63,
            "fields": {
                "name": "Lorem ipsum dolor sit amet, consectetuer adipiscing",
                "description": "JXgLtkjalmq ZeqXSKnaLI efUCKJvQ lWECyrvPbZiV KfZpsrQJRelk rnsoJA SqkXsdo mEoXNM DfbyCSXjI nrXiT rtIZRxLSpe WTDBRuK RaciqW PbfvpdN"
            }
        },
        {
            "model": "items.Item",
            "pk": 64,
            "fields": {
                "name": "semper egestas, urna justo faucibus",
                "description": "VRTbyenvgAB SjXAbZLwalc jXbwe oeSXyRt FyIKgluRZ NSAB HvRONCpPtiF pZLVMSfsj fbqYOaMZmw"
            }
        },
        {
            "model": "items.Item",
            "pk": 65,
            "fields": {
                "name": "Cras dolor dolor, tempus non, lacinia at, iaculis quis, pede.",
                "description": "HLgySFDpvT bKcG bvKAY wagVIJ ViPSJqZycm"
            }
        },
        {
            "model": "items.Item",
            "pk": 66,
            "fields": {
                "name": "mi tempor lorem, eget mollis lectus pede et risus.",
                "description": "YwSiGURr AgOJxvRH joaCmT ZAwHGjbv QMYN KAZhHLJSOENT XfdgoRDMYKPu zPFVciQI QBaClUhiXd wTJqHb"
            }
        },
        {
            "model": "items.Item",
            "pk": 67,
            "fields": {
                "name": "Nunc sollicitudin commodo ipsum. Suspendisse",
                "description": "NJZnAgXqyKv WFPbNgplzoqJ Cshpt RMTGAtKfp aBEw dLSUy rvKUAIL INrSCKwGB gATId aTVdU eQthuUBPfCwS kcolJH CJrlqNi UlnTharFi"
            }
        },
        {
            "model": "items.Item",
            "pk": 68,
            "fields": {
                "name": "nisl. Quisque fringilla euismod enim.",
                "description": "hZevpfDLSJ TWaIDvUwsXdu xhBdnaCVp yzETWxRQs RyrkmVHnqMg POCSYM XYFSMvoLewW RudfIL AbiQP FWlbt gQbHteldK"
            }
        },
        {
            "model": "items.Item",
            "pk": 69,
            "fields": {
                "name": "felis orci, adipiscing non, luctus",
                "description": "NDrGovzM VhYpMNWEuH fhwStCi hBCRwv"
            }
        },
        {
            "model": "items.Item",
            "pk": 70,
            "fields": {
                "name": "convallis",
                "description": "Lyfbd venugYUZEoRX nljNua yueTLipYAl SnrZgQaNBzC qvHQnCm rOeSEbAl Qovepb zuIiXgBbL XTQvfq tUnpa WXPdtCKRuT zWERcmKiSwb TltG"
            }
        },
        {
            "model": "items.Item",
            "pk": 71,
            "fields": {
                "name": "tortor at risus. Nunc ac sem ut dolor dapibus gravida.",
                "description": "rMugJP bzNJaqdUg BmiKCdMYkGqT ZHpEuUWlfbsm YiGyqrn cjpXgHEoDUB GqHoSERBLciU gNQVMyDt WMLJUr vpTVuPzye JOcqUmHVTz"
            }
        },
        {
            "model": "items.Item",
            "pk": 72,
            "fields": {
                "name": "nunc. In at pede. Cras",
                "description": "urvFomKQx ctsNGfp wcLdQnqJkpSK wgOqVuZDQ"
            }
        },
        {
            "model": "items.Item",
            "pk": 73,
            "fields": {
                "name": "lorem lorem, luctus ut, pellentesque eget, dictum placerat, augue.",
                "description": "CfPXEQ qgVIAEpoF vjBW WgiHyOz IrlOeQPofL VbiKmWywB vwiukrh NLUPJqCVe diSEOoKQmbvV axYNiKMZy GTwqp VrYm OukyzHn ixyGVD ktFJSqxoZ"
            }
        },
        {
            "model": "items.Item",
            "pk": 74,
            "fields": {
                "name": "eget magna. Suspendisse tristique neque venenatis lacus. Etiam",
                "description": "fFTLN hoIv fFri PXHs zFXxftciq tAOHgWbShETI gQGRxFNOfSEe uKCyT ksQrY"
            }
        },
        {
            "model": "items.Item",
            "pk": 75,
            "fields": {
                "name": "nascetur ridiculus",
                "description": "kqTJaXO ztPcyxS HXmZFdtWz STEnGQsmiotZ supalBYNOVJr vwqNjT jQaq FbuRwqBySa IcFaljfMUt cNSZEtIjFV wjlSFNDromJs yZQbRFs KgbhBY"
            }
        },
        {
            "model": "items.Item",
            "pk": 76,
            "fields": {
                "name": "odio. Aliquam vulputate",
                "description": "amZskqP tOgheP PYfKWnLCbeF UucVtaP"
            }
        },
        {
            "model": "items.Item",
            "pk": 77,
            "fields": {
                "name": "neque. Sed eget lacus. Mauris non",
                "description": "zrNMw uTUIR WwAlRsHcPh LesAH ZQFPv DgKXL IAcMipZJgjl uYJhqeEHWTSZ SkyG YiJTxwEMDc iBbcfH"
            }
        },
        {
            "model": "items.Item",
            "pk": 78,
            "fields": {
                "name": "dui. Fusce diam nunc,",
                "description": "VxMed wpKI hGcOvuAQ MdWeUolGqp LnMKfjYes pqWIKz jUIqbfHkT xosJbpDaR bsnKueCUp LbBQVfJT IRMF pTrGCbXRdcN"
            }
        },
        {
            "model": "items.Item",
            "pk": 79,
            "fields": {
                "name": "quam a felis ullamcorper viverra. Maecenas iaculis aliquet diam. Sed",
                "description": "rxWcsOIyie PJFhwLKNt xUqLZayjHDFr pQqDuUchF ZQMALjHB QuKVYvfHSh"
            }
        },
        {
            "model": "items.Item",
            "pk": 80,
            "fields": {
                "name": "a, auctor non, feugiat nec, diam. Duis mi enim,",
                "description": "WGFCPELVhzK Zain sKthLxAS ECXu dnwzOJsFSbRN wfnIOHbRQs WeXlRgqpLu YKxwNZqcIr MjLhimJwW FlIeCpvnEOi ismoGvMKxFyJ"
            }
        },
        {
            "model": "items.Item",
            "pk": 81,
            "fields": {
                "name": "adipiscing, enim mi tempor lorem, eget mollis lectus pede",
                "description": "fiCsBL jntiqH tauXPmZvJCL MxJbnUoa TczqkpmLdE EAUfYPGRry MedATuBjfWz ywhSsxB wRsixv AtjU jCzUlqPpLX hgMLTriaoS DtSjvUqwGHkh XAMrDpSPcT KqStupGObfTd"
            }
        },
        {
            "model": "items.Item",
            "pk": 82,
            "fields": {
                "name": "sed leo. Cras vehicula",
                "description": "supFUv CXlWakf ywkdnfZE"
            }
        },
        {
            "model": "items.Item",
            "pk": 83,
            "fields": {
                "name": "at sem molestie sodales. Mauris blandit enim consequat purus. Maecenas",
                "description": "NiPmWf BGMHsObdU ZLnGPUVYbIm NTZrmHDUxiIM"
            }
        },
        {
            "model": "items.Item",
            "pk": 84,
            "fields": {
                "name": "Nunc quis arcu",
                "description": "XGHqpEjI bNYtTIPB endYGuA bjgO pmTkRgF wPqnL ezps SPidkl UKuYFlbZs oXucGZMjkt efHzkYL oYKTubhBZE otIEGaM OzSq"
            }
        },
        {
            "model": "items.Item",
            "pk": 85,
            "fields": {
                "name": "In scelerisque scelerisque dui. Suspendisse ac metus",
                "description": "guvBRND qKGloW IrZskSiOPxMU ZxYPtEGXl HUNG"
            }
        },
        {
            "model": "items.Item",
            "pk": 86,
            "fields": {
                "name": "Cras sed leo. Cras vehicula aliquet libero. Integer in",
                "description": "VScAPLdNCK mUnRLq uRfNgrxGe XsWlYfwB HasvLE RnhG SzNfUZxT Lzsg IDTq DRhGtpjxBb JYnljmg"
            }
        },
        {
            "model": "items.Item",
            "pk": 87,
            "fields": {
                "name": "neque tellus, imperdiet non, vestibulum nec, euismod",
                "description": "DkQZRTgJOl BimGZgqVA WCIuaB JxyZaEpInr yuBedi kGtKz ChLmizO pLcYWu mHVKs"
            }
        },
        {
            "model": "items.Item",
            "pk": 88,
            "fields": {
                "name": "natoque penatibus et",
                "description": "PeoGBu BuaArKbNj BToZtupCg KiRPMcNxzD priZJex imUbELK GtqbpYiPU qaEKnrkFPoyC"
            }
        },
        {
            "model": "items.Item",
            "pk": 89,
            "fields": {
                "name": "nec orci. Donec nibh. Quisque nonummy ipsum non",
                "description": "NJRZIGln STfkR XWkBarbqJUO pMxr GRvMhAFX fFGVCabDr qEvlpG WeNlyZqfYoJ qKgNzrfPS ifGD"
            }
        },
        {
            "model": "items.Item",
            "pk": 90,
            "fields": {
                "name": "ac mi eleifend egestas.",
                "description": "RCOjbfDg mDXpZBYuGsRg yEQCVX JATRCe kLrzdOn ISdgq OiNYBqtHGJdm jZOyqkM GYFKoNgw GBMRQXE odMSER FfYpxS"
            }
        },
        {
            "model": "items.Item",
            "pk": 91,
            "fields": {
                "name": "nec quam. Curabitur vel lectus. Cum",
                "description": "CXFVSxGfmoWH dIzQHl FGQdPXASYvre hGSVORdLMCc UxAqkboI dMLnRcPmG tYdOgGiLMETb doWMZ gaZKLEo"
            }
        },
        {
            "model": "items.Item",
            "pk": 92,
            "fields": {
                "name": "malesuada fames ac turpis egestas. Aliquam fringilla cursus",
                "description": "kLqpWsYyJSg NALkCRFaIBg RVHpwkS SBnNqxROCya hoNxWVJ ErBfO uvEbP mtGHZDELgC lIGQ zNwJdoftV aLAQ QJYPo"
            }
        },
        {
            "model": "items.Item",
            "pk": 93,
            "fields": {
                "name": "Cum sociis natoque penatibus et magnis",
                "description": "blLa RTzLkuh USRl zbJq vSeclJiZYzC zUfsn nUOt yCiEajZdB aXdm"
            }
        },
        {
            "model": "items.Item",
            "pk": 94,
            "fields": {
                "name": "tincidunt aliquam arcu.",
                "description": "nvsxGgdelHZa OPVyLKR mkPcQtL zmuMX gvXEsTKDmRnL bGLqKBDyACZf VEKZgas CrTQoLEUyNqc FzbBvIlP kRWX GjBs CxQrWuwDEpmi krBZKIng iKnbxz rpqAsPN"
            }
        },
        {
            "model": "items.Item",
            "pk": 95,
            "fields": {
                "name": "justo sit amet nulla. Donec non justo.",
                "description": "zolHxAp wjliYvUfdPy KSpNvWErJslc snQrOghbT IStyYuPDrX FGgP fNyZEGTm BAyCaL iFectSEZhms npSojRT YPFdTripAJD"
            }
        },
        {
            "model": "items.Item",
            "pk": 96,
            "fields": {
                "name": "lectus quis",
                "description": "EUQWnD OgVwehAQxNU vpeibRBkWLqK QAKWw iSPtIOsF vpgNskz zPDvKVX"
            }
        },
        {
            "model": "items.Item",
            "pk": 97,
            "fields": {
                "name": "fermentum vel,",
                "description": "PAQoDzhyVXY jOflYnFzhV ksgcOKlyZie"
            }
        },
        {
            "model": "items.Item",
            "pk": 98,
            "fields": {
                "name": "Etiam gravida",
                "description": "uiRGXafhHW fnrEcs vXMHpN beLQxaEU mJwFAuDl ruCWM qkGmCVE jHtLCWl mPeMIiJWq jsOGqYeLimvb nUbYAlmV"
            }
        },
        {
            "model": "items.Item",
            "pk": 99,
            "fields": {
                "name": "eu metus. In lorem. Donec elementum, lorem ut aliquam iaculis,",
                "description": "pirs VzmDbdKwj Rfqh NRBHYJjxuL VXprelyoOv fiuGUJq bKAgxOmw wRPtyh LRUnyg iKeUduyq"
            }
        },
        {
            "model": "items.Item",
            "pk": 100,
            "fields": {
                "name": "euismod in,",
                "description": "COiJFDbyUS YlcqrbNxEKvh xBIvzLhGPFQ YMWIlVGPcy zBGjMQYETKRl PGnLD objwxTRIy pfcYmQBa ladrMYBsSm TFgPj mvkMIQjy nZFqN ZlUDiCfqVo jvdPif"
            }
        },
        {
            "model": "items.Part",
            "pk": 1,
            "fields": {
                "name": "TNM KUnNvD",
                "item": 1
            }
        },
        {
            "model": "items.Part",
            "pk": 2,
            "fields": {
                "name": "woYFgfZ DVGrF JgsIr uN PGx xTwduv",
                "item": 1
            }
        },
        {
            "model": "items.Part",
            "pk": 3,
            "fields": {
                "name": "NLdsMFu ak rgTC lFBNQ ZQ HUuZIthq",
                "item": 2
            }
        },
        {
            "model": "items.Part",
            "pk": 4,
            "fields": {
                "name": "rjY xEvIj rFLPl bVqdBS mox ZOYk MwGegmU",
                "item": 2
            }
        },
        {
            "model": "items.Part",
            "pk": 5,
            "fields": {
                "name": "ORFxbmC HcLshW cbIRyU UXBEM vCwc hjcuMBRI hRxsTjL",
                "item": 3
            }
        },
        {
            "model": "items.Part",
            "pk": 6,
            "fields": {
                "name": "od yLmwtn Iqsf",
                "item": 3
            }
        },
        {
            "model": "items.Part",
            "pk": 7,
            "fields": {
                "name": "GHxACaz",
                "item": 4
            }
        },
        {
            "model": "items.Part",
            "pk": 8,
            "fields": {
                "name": "BKywOo UWZ xws M YCTZUI gGk",
                "item": 5
            }
        },
        {
            "model": "items.Part",
            "pk": 9,
            "fields": {
                "name": "OimYGL exgMYjLa O flbMB tTiUFW PYCQSoj HMdLhRBT",
                "item": 5
            }
        },
        {
            "model": "items.Part",
            "pk": 10,
            "fields": {
                "name": "FMTG EFs PEnUO yGO f",
                "item": 6
            }
        },
        {
            "model": "items.Part",
            "pk": 11,
            "fields": {
                "name": "Vkdl bQLRgvaU taVnKg u A V qyuZbw",
                "item": 6
            }
        },
        {
            "model": "items.Part",
            "pk": 12,
            "fields": {
                "name": "FxCef yY EaWo pDs tsgXhbR",
                "item": 6
            }
        },
        {
            "model": "items.Part",
            "pk": 13,
            "fields": {
                "name": "wuQ t",
                "item": 7
            }
        },
        {
            "model": "items.Part",
            "pk": 14,
            "fields": {
                "name": "hNFwsPKQ azfWB",
                "item": 8
            }
        },
        {
            "model": "items.Part",
            "pk": 15,
            "fields": {
                "name": "fg UlACPrY",
                "item": 9
            }
        },
        {
            "model": "items.Part",
            "pk": 16,
            "fields": {
                "name": "fOxQCcsM mxqEU",
                "item": 9
            }
        },
        {
            "model": "items.Part",
            "pk": 17,
            "fields": {
                "name": "LiGEky ejq",
                "item": 9
            }
        },
        {
            "model": "items.Part",
            "pk": 18,
            "fields": {
                "name": "TxG oh iCGfncg GVuSWdm cPAsr a",
                "item": 10
            }
        },
        {
            "model": "items.Part",
            "pk": 19,
            "fields": {
                "name": "F YI",
                "item": 11
            }
        },
        {
            "model": "items.Part",
            "pk": 20,
            "fields": {
                "name": "gJqZpTvV uJLCl lCdmMB xk liuVknWj rHUSX",
                "item": 11
            }
        },
        {
            "model": "items.Part",
            "pk": 21,
            "fields": {
                "name": "w AQHMWw",
                "item": 11
            }
        },
        {
            "model": "items.Part",
            "pk": 22,
            "fields": {
                "name": "qkHlJaD t ueXqdb oOy InLUXQyi DBsw",
                "item": 12
            }
        },
        {
            "model": "items.Part",
            "pk": 23,
            "fields": {
                "name": "MuDz xYmQnwlD WgD aOMSXKb QPJimO z ctZE",
                "item": 13
            }
        },
        {
            "model": "items.Part",
            "pk": 24,
            "fields": {
                "name": "XlRA asZ Mw",
                "item": 14
            }
        },
        {
            "model": "items.Part",
            "pk": 25,
            "fields": {
                "name": "jLxckI fnQJDpY",
                "item": 14
            }
        },
        {
            "model": "items.Part",
            "pk": 26,
            "fields": {
                "name": "fsL vtwhepX dUKXvYNT MsPZxSrq UgKu",
                "item": 15
            }
        },
        {
            "model": "items.Part",
            "pk": 27,
            "fields": {
                "name": "zWCU QRp zNcvfC vT",
                "item": 15
            }
        },
        {
            "model": "items.Part",
            "pk": 28,
            "fields": {
                "name": "aVm YSd ufI EMW s",
                "item": 16
            }
        },
        {
            "model": "items.Part",
            "pk": 29,
            "fields": {
                "name": "BIKs YlCVX nvGOEVWt LeaYNDy tyD HfmG",
                "item": 16
            }
        },
        {
            "model": "items.Part",
            "pk": 30,
            "fields": {
                "name": "nTo lUVz riQdzgyt mo QAOjSoJ EweGUb MHnV",
                "item": 16
            }
        },
        {
            "model": "items.Part",
            "pk": 31,
            "fields": {
                "name": "QsxeNtB LPoub",
                "item": 17
            }
        },
        {
            "model": "items.Part",
            "pk": 32,
            "fields": {
                "name": "FSq",
                "item": 17
            }
        },
        {
            "model": "items.Part",
            "pk": 33,
            "fields": {
                "name": "THlRLID crkLnpO oNXCHg LptKRH fHtL eORJ",
                "item": 17
            }
        },
        {
            "model": "items.Part",
            "pk": 34,
            "fields": {
                "name": "c p qyULJxbe raNt zMFL DEItZU",
                "item": 18
            }
        },
        {
            "model": "items.Part",
            "pk": 35,
            "fields": {
                "name": "yzWDPhx oG mVyrsaN xp ISvGVCP",
                "item": 19
            }
        },
        {
            "model": "items.Part",
            "pk": 36,
            "fields": {
                "name": "EBFG an i OyP hry",
                "item": 20
            }
        },
        {
            "model": "items.Part",
            "pk": 37,
            "fields": {
                "name": "d",
                "item": 20
            }
        },
        {
            "model": "items.Part",
            "pk": 38,
            "fields": {
                "name": "kRHayQd xhdvmit EDGcBqV TrkNFZ ertP rU",
                "item": 20
            }
        },
        {
            "model": "items.Part",
            "pk": 39,
            "fields": {
                "name": "RTXtgaD TXMkK jRQwTuc yu bkKOmsa ZsLWYBHS",
                "item": 21
            }
        },
        {
            "model": "items.Part",
            "pk": 40,
            "fields": {
                "name": "m gOJrZpDA TAVrKC qlBvX ZwQWojB",
                "item": 21
            }
        },
        {
            "model": "items.Part",
            "pk": 41,
            "fields": {
                "name": "OhXQwmHx CABsgVDI EKaBA x NFBKOT joDLaM",
                "item": 22
            }
        },
        {
            "model": "items.Part",
            "pk": 42,
            "fields": {
                "name": "npQAIhf FjacKz hbWDwG IicMPqpK EWYQmj YXz hlUsvjBO",
                "item": 22
            }
        },
        {
            "model": "items.Part",
            "pk": 43,
            "fields": {
                "name": "XlUfMZz zatyPjg jtrJDm sFYXb vdoZx",
                "item": 22
            }
        },
        {
            "model": "items.Part",
            "pk": 44,
            "fields": {
                "name": "GNLDc brxuT GTEiFgU k bthdY",
                "item": 23
            }
        },
        {
            "model": "items.Part",
            "pk": 45,
            "fields": {
                "name": "Qw itC pIgwi",
                "item": 23
            }
        },
        {
            "model": "items.Part",
            "pk": 46,
            "fields": {
                "name": "eKQNchM nGWOP Phs iSNysawZ",
                "item": 24
            }
        },
        {
            "model": "items.Part",
            "pk": 47,
            "fields": {
                "name": "kxnTvE qvHPSpA dIFj eAPqBt fGV nFYKu cZIAzRkt",
                "item": 24
            }
        },
        {
            "model": "items.Part",
            "pk": 48,
            "fields": {
                "name": "KZ",
                "item": 25
            }
        },
        {
            "model": "items.Part",
            "pk": 49,
            "fields": {
                "name": "IoCk",
                "item": 25
            }
        },
        {
            "model": "items.Part",
            "pk": 50,
            "fields": {
                "name": "QuXIhm Z rHZzUghI",
                "item": 25
            }
        },
        {
            "model": "items.Part",
            "pk": 51,
            "fields": {
                "name": "j CXlQJV EesGlgL Am nrfkAvE",
                "item": 26
            }
        },
        {
            "model": "items.Part",
            "pk": 52,
            "fields": {
                "name": "Dsozj AMD",
                "item": 26
            }
        },
        {
            "model": "items.Part",
            "pk": 53,
            "fields": {
                "name": "pqjSznA av Tlegq AEa jdYDq",
                "item": 26
            }
        },
        {
            "model": "items.Part",
            "pk": 54,
            "fields": {
                "name": "b MLVZiWN MQrGK Bzl gYHTUDI KEzyrdnY",
                "item": 27
            }
        },
        {
            "model": "items.Part",
            "pk": 55,
            "fields": {
                "name": "DuoXNcJs Qeu",
                "item": 27
            }
        },
        {
            "model": "items.Part",
            "pk": 56,
            "fields": {
                "name": "ua wVj AFP y Vxe hoHtFEjM",
                "item": 28
            }
        },
        {
            "model": "items.Part",
            "pk": 57,
            "fields": {
                "name": "PvFBuf",
                "item": 29
            }
        },
        {
            "model": "items.Part",
            "pk": 58,
            "fields": {
                "name": "wLhoq HQpTm",
                "item": 30
            }
        },
        {
            "model": "items.Part",
            "pk": 59,
            "fields": {
                "name": "SRUE",
                "item": 31
            }
        },
        {
            "model": "items.Part",
            "pk": 60,
            "fields": {
                "name": "W B",
                "item": 31
            }
        },
        {
            "model": "items.Part",
            "pk": 61,
            "fields": {
                "name": "fO KNaDz",
                "item": 32
            }
        },
        {
            "model": "items.Part",
            "pk": 62,
            "fields": {
                "name": "ls JlNp YDghUXW FpRhxSk",
                "item": 33
            }
        },
        {
            "model": "items.Part",
            "pk": 63,
            "fields": {
                "name": "Onh ZuESiM M",
                "item": 33
            }
        },
        {
            "model": "items.Part",
            "pk": 64,
            "fields": {
                "name": "APJcGFt sP XK",
                "item": 34
            }
        },
        {
            "model": "items.Part",
            "pk": 65,
            "fields": {
                "name": "ahstnTK sjQI wMk HViKzf",
                "item": 34
            }
        },
        {
            "model": "items.Part",
            "pk": 66,
            "fields": {
                "name": "qHzMWTpO uXEa shCuOk",
                "item": 34
            }
        },
        {
            "model": "items.Part",
            "pk": 67,
            "fields": {
                "name": "SFLk PSGUHEa bzPKmYJ",
                "item": 35
            }
        },
        {
            "model": "items.Part",
            "pk": 68,
            "fields": {
                "name": "geZ",
                "item": 36
            }
        },
        {
            "model": "items.Part",
            "pk": 69,
            "fields": {
                "name": "zbrt LPBnZ mDF lkFeoj JxjMe e",
                "item": 36
            }
        },
        {
            "model": "items.Part",
            "pk": 70,
            "fields": {
                "name": "pevcG",
                "item": 36
            }
        },
        {
            "model": "items.Part",
            "pk": 71,
            "fields": {
                "name": "OtWLHouU U uRPyYgj rTtVGyFC g DEp",
                "item": 37
            }
        },
        {
            "model": "items.Part",
            "pk": 72,
            "fields": {
                "name": "VCHd cBIkq rGfB yPVUaI Ev",
                "item": 38
            }
        },
        {
            "model": "items.Part",
            "pk": 73,
            "fields": {
                "name": "oe FRAlC MzE Us hsFPAaru HGyUBvib gq",
                "item": 39
            }
        },
        {
            "model": "items.Part",
            "pk": 74,
            "fields": {
                "name": "PDMRG zJFH VAicLkto JGCY GnuKh YtLy",
                "item": 39
            }
        },
        {
            "model": "items.Part",
            "pk": 75,
            "fields": {
                "name": "Ne UWgKZto x HIeFO XiwNnDdg YZAKP",
                "item": 40
            }
        },
        {
            "model": "items.Part",
            "pk": 76,
            "fields": {
                "name": "v wvBTdSJH FwZMi",
                "item": 40
            }
        },
        {
            "model": "items.Part",
            "pk": 77,
            "fields": {
                "name": "y",
                "item": 41
            }
        },
        {
            "model": "items.Part",
            "pk": 78,
            "fields": {
                "name": "Xh q vCnWu f",
                "item": 41
            }
        },
        {
            "model": "items.Part",
            "pk": 79,
            "fields": {
                "name": "qJWzYpSj Xusq Eb N HIO",
                "item": 41
            }
        },
        {
            "model": "items.Part",
            "pk": 80,
            "fields": {
                "name": "d ewauIosd AjbzN AhGVOtD hpO AWcih esavbgz",
                "item": 42
            }
        },
        {
            "model": "items.Part",
            "pk": 81,
            "fields": {
                "name": "ToWnc uWPzNaso oalbMw TjqHMfr yvU",
                "item": 42
            }
        },
        {
            "model": "items.Part",
            "pk": 82,
            "fields": {
                "name": "eNmIRb",
                "item": 42
            }
        },
        {
            "model": "items.Part",
            "pk": 83,
            "fields": {
                "name": "HXGKkC RiTx TxOXys FNAnh XfD LCKUtQ",
                "item": 43
            }
        },
        {
            "model": "items.Part",
            "pk": 84,
            "fields": {
                "name": "oyDlCH qK WrS",
                "item": 43
            }
        },
        {
            "model": "items.Part",
            "pk": 85,
            "fields": {
                "name": "Hy",
                "item": 44
            }
        },
        {
            "model": "items.Part",
            "pk": 86,
            "fields": {
                "name": "MV UXzgqvL m mIgK",
                "item": 44
            }
        },
        {
            "model": "items.Part",
            "pk": 87,
            "fields": {
                "name": "iOLk zGOX nal",
                "item": 44
            }
        },
        {
            "model": "items.Part",
            "pk": 88,
            "fields": {
                "name": "qeKhR Cp iJ jiEbUkGF ApjTy ABybaEP LO",
                "item": 45
            }
        },
        {
            "model": "items.Part",
            "pk": 89,
            "fields": {
                "name": "HrElgTZP",
                "item": 46
            }
        },
        {
            "model": "items.Part",
            "pk": 90,
            "fields": {
                "name": "TqZxYWXO kznBtK RtU ePO eXu",
                "item": 47
            }
        },
        {
            "model": "items.Part",
            "pk": 91,
            "fields": {
                "name": "GNL Rwegcr",
                "item": 47
            }
        },
        {
            "model": "items.Part",
            "pk": 92,
            "fields": {
                "name": "hVBnQEw Y N QsMF ODzMEtX",
                "item": 47
            }
        },
        {
            "model": "items.Part",
            "pk": 93,
            "fields": {
                "name": "tP GfHIsVmF HCfs qyvcd",
                "item": 48
            }
        },
        {
            "model": "items.Part",
            "pk": 94,
            "fields": {
                "name": "IWiFKZDY lJuGM TNQd",
                "item": 48
            }
        },
        {
            "model": "items.Part",
            "pk": 95,
            "fields": {
                "name": "c",
                "item": 49
            }
        },
        {
            "model": "items.Part",
            "pk": 96,
            "fields": {
                "name": "WLuUYl xO htnuwiv Gzhd wHrMPDQY rguNs",
                "item": 50
            }
        },
        {
            "model": "items.Part",
            "pk": 97,
            "fields": {
                "name": "hnY bxsnvm HuqaR w zfEWHGSI",
                "item": 50
            }
        },
        {
            "model": "items.Part",
            "pk": 98,
            "fields": {
                "name": "oYTs MxysIJp EcLhBp mTS iv vlU",
                "item": 51
            }
        },
        {
            "model": "items.Part",
            "pk": 99,
            "fields": {
                "name": "HKNnzlv hSfClik yFi TPSRVu",
                "item": 51
            }
        },
        {
            "model": "items.Part",
            "pk": 100,
            "fields": {
                "name": "aNewUtJ uQOry F hIRy BNyGmZ agkS ij",
                "item": 51
            }
        },
        {
            "model": "items.Part",
            "pk": 101,
            "fields": {
                "name": "AwNe",
                "item": 52
            }
        },
        {
            "model": "items.Part",
            "pk": 102,
            "fields": {
                "name": "BGoyA viZz halBLyx PzKqL",
                "item": 53
            }
        },
        {
            "model": "items.Part",
            "pk": 103,
            "fields": {
                "name": "HJCM eZdzMLOk dMesai owtkaTI",
                "item": 54
            }
        },
        {
            "model": "items.Part",
            "pk": 104,
            "fields": {
                "name": "nBKrx gHAepZJ cV cdLAoDts",
                "item": 55
            }
        },
        {
            "model": "items.Part",
            "pk": 105,
            "fields": {
                "name": "fpu tpuXyREs ODiBSM UQAdP okMcg Dbj",
                "item": 56
            }
        },
        {
            "model": "items.Part",
            "pk": 106,
            "fields": {
                "name": "MXohc gj D OHTmwu hUI",
                "item": 56
            }
        },
        {
            "model": "items.Part",
            "pk": 107,
            "fields": {
                "name": "ADjpxBy dRpuF rioG jHnR",
                "item": 56
            }
        },
        {
            "model": "items.Part",
            "pk": 108,
            "fields": {
                "name": "wjIrB mH dADwPOJB Xw",
                "item": 57
            }
        },
        {
            "model": "items.Part",
            "pk": 109,
            "fields": {
                "name": "vNM",
                "item": 58
            }
        },
        {
            "model": "items.Part",
            "pk": 110,
            "fields": {
                "name": "trY",
                "item": 58
            }
        },
        {
            "model": "items.Part",
            "pk": 111,
            "fields": {
                "name": "YdRHkOC yx A Vj Gln tKelwU",
                "item": 58
            }
        },
        {
            "model": "items.Part",
            "pk": 112,
            "fields": {
                "name": "V RSyUAoX oHh hetX m PGI",
                "item": 59
            }
        },
        {
            "model": "items.Part",
            "pk": 113,
            "fields": {
                "name": "WzyCFNr tmOTBNfv xpgBHrA",
                "item": 59
            }
        },
        {
            "model": "items.Part",
            "pk": 114,
            "fields": {
                "name": "WwLHNoAj",
                "item": 60
            }
        },
        {
            "model": "items.Part",
            "pk": 115,
            "fields": {
                "name": "jhFNRJY",
                "item": 60
            }
        },
        {
            "model": "items.Part",
            "pk": 116,
            "fields": {
                "name": "OJu guBcyjiY RHxLmn udFoHyi",
                "item": 61
            }
        },
        {
            "model": "items.Part",
            "pk": 117,
            "fields": {
                "name": "OfEmWcH",
                "item": 61
            }
        },
        {
            "model": "items.Part",
            "pk": 118,
            "fields": {
                "name": "TNatfgF J od kA KwRJYB xAKHL DNXAWRsM",
                "item": 61
            }
        },
        {
            "model": "items.Part",
            "pk": 119,
            "fields": {
                "name": "SMkQNDUj Kgp hGQc hAu",
                "item": 62
            }
        },
        {
            "model": "items.Part",
            "pk": 120,
            "fields": {
                "name": "rl gOuGjdn vqyelW wbloCe",
                "item": 62
            }
        },
        {
            "model": "items.Part",
            "pk": 121,
            "fields": {
                "name": "X k KSLuQdJ OSpKNqC uP pHu",
                "item": 62
            }
        },
        {
            "model": "items.Part",
            "pk": 122,
            "fields": {
                "name": "dHvg Y Ql mtPk QkjfLhg",
                "item": 63
            }
        },
        {
            "model": "items.Part",
            "pk": 123,
            "fields": {
                "name": "JG d FSX gFAJES rxvJcu HNLjIpmW DzTjI",
                "item": 63
            }
        },
        {
            "model": "items.Part",
            "pk": 124,
            "fields": {
                "name": "bhiWmXR TuevOtA",
                "item": 64
            }
        },
        {
            "model": "items.Part",
            "pk": 125,
            "fields": {
                "name": "gBwYJ irTygwAP D AskUfiXp XKGz MwLNXO uCqc",
                "item": 64
            }
        },
        {
            "model": "items.Part",
            "pk": 126,
            "fields": {
                "name": "GQHgrExp usBQJmLR YH Oq VCY KGVpZsOg hiDAN",
                "item": 65
            }
        },
        {
            "model": "items.Part",
            "pk": 127,
            "fields": {
                "name": "rit GmeW lnpHstF h eVisIyaF M gfa",
                "item": 65
            }
        },
        {
            "model": "items.Part",
            "pk": 128,
            "fields": {
                "name": "vVgrFl jLZuWzp WtxNY",
                "item": 65
            }
        },
        {
            "model": "items.Part",
            "pk": 129,
            "fields": {
                "name": "lXuKk O",
                "item": 66
            }
        },
        {
            "model": "items.Part",
            "pk": 130,
            "fields": {
                "name": "a AEBp",
                "item": 66
            }
        },
        {
            "model": "items.Part",
            "pk": 131,
            "fields": {
                "name": "wUI jN",
                "item": 66
            }
        },
        {
            "model": "items.Part",
            "pk": 132,
            "fields": {
                "name": "Onk JkXxmlwM SRgEsPwp",
                "item": 67
            }
        },
        {
            "model": "items.Part",
            "pk": 133,
            "fields": {
                "name": "RDmKS yxHY zlXf m bRPD VJZUDujO",
                "item": 68
            }
        },
        {
            "model": "items.Part",
            "pk": 134,
            "fields": {
                "name": "uFVI aeYZ whIu y",
                "item": 68
            }
        },
        {
            "model": "items.Part",
            "pk": 135,
            "fields": {
                "name": "CNoOUYKM dHGLWB sYQEB Nue",
                "item": 68
            }
        },
        {
            "model": "items.Part",
            "pk": 136,
            "fields": {
                "name": "RNiJucX",
                "item": 69
            }
        },
        {
            "model": "items.Part",
            "pk": 137,
            "fields": {
                "name": "Lh uRSa IsNg gdropXxj uVyhj",
                "item": 69
            }
        },
        {
            "model": "items.Part",
            "pk": 138,
            "fields": {
                "name": "VDhg pzZFWDr RFKByDjJ VjQ YZaEDs uMC",
                "item": 69
            }
        },
        {
            "model": "items.Part",
            "pk": 139,
            "fields": {
                "name": "HFYUSLp",
                "item": 70
            }
        },
        {
            "model": "items.Part",
            "pk": 140,
            "fields": {
                "name": "k FM sRfQOXd tKNEsq GBpulS jNyL",
                "item": 71
            }
        },
        {
            "model": "items.Part",
            "pk": 141,
            "fields": {
                "name": "PInDi fQb UzcrdDMm Ru qLx",
                "item": 71
            }
        },
        {
            "model": "items.Part",
            "pk": 142,
            "fields": {
                "name": "DSwip k KQf qlSBaTk",
                "item": 71
            }
        },
        {
            "model": "items.Part",
            "pk": 143,
            "fields": {
                "name": "Lzvrm rdFetZU YAUjrioT WlYAOfy",
                "item": 72
            }
        },
        {
            "model": "items.Part",
            "pk": 144,
            "fields": {
                "name": "zaJVwKv Dvgwn ed nBx NBUAzy",
                "item": 72
            }
        },
        {
            "model": "items.Part",
            "pk": 145,
            "fields": {
                "name": "YrOMg",
                "item": 73
            }
        },
        {
            "model": "items.Part",
            "pk": 146,
            "fields": {
                "name": "gVbWEN zWnrxYO LZ",
                "item": 73
            }
        },
        {
            "model": "items.Part",
            "pk": 147,
            "fields": {
                "name": "v vW UZhHfs ig",
                "item": 74
            }
        },
        {
            "model": "items.Part",
            "pk": 148,
            "fields": {
                "name": "Q Mpj r eBR m YEIj cnRjF",
                "item": 74
            }
        },
        {
            "model": "items.Part",
            "pk": 149,
            "fields": {
                "name": "uwSRaDt",
                "item": 74
            }
        },
        {
            "model": "items.Part",
            "pk": 150,
            "fields": {
                "name": "MBya Dv QopPkOaL Jqe nP qUajYXny",
                "item": 75
            }
        },
        {
            "model": "items.Part",
            "pk": 151,
            "fields": {
                "name": "WT",
                "item": 75
            }
        },
        {
            "model": "items.Part",
            "pk": 152,
            "fields": {
                "name": "Wo mER wSNdOQc D gXT",
                "item": 75
            }
        },
        {
            "model": "items.Part",
            "pk": 153,
            "fields": {
                "name": "Hxyig EHodV",
                "item": 76
            }
        },
        {
            "model": "items.Part",
            "pk": 154,
            "fields": {
                "name": "MHd bq nwV hcy",
                "item": 76
            }
        },
        {
            "model": "items.Part",
            "pk": 155,
            "fields": {
                "name": "dTEGvLA",
                "item": 76
            }
        },
        {
            "model": "items.Part",
            "pk": 156,
            "fields": {
                "name": "n fkGQTM uhpTPWjz Eoch",
                "item": 77
            }
        },
        {
            "model": "items.Part",
            "pk": 157,
            "fields": {
                "name": "rxEjSv bf TC EYPTG FJIjx ifYXBUda",
                "item": 77
            }
        },
        {
            "model": "items.Part",
            "pk": 158,
            "fields": {
                "name": "KdQkvmOy VDRbvpnq la cwCWshGV CEeYO",
                "item": 77
            }
        },
        {
            "model": "items.Part",
            "pk": 159,
            "fields": {
                "name": "XByalV kIWMveD mEc SdI rU CBMZ Ga",
                "item": 78
            }
        },
        {
            "model": "items.Part",
            "pk": 160,
            "fields": {
                "name": "GRpF dCtHRo FuIgOZy OwgEvB eZmVzv SblT jNnPKRG",
                "item": 78
            }
        },
        {
            "model": "items.Part",
            "pk": 161,
            "fields": {
                "name": "OaEYUJnb hy fWhJaAC bq fQYv tB mBge",
                "item": 79
            }
        },
        {
            "model": "items.Part",
            "pk": 162,
            "fields": {
                "name": "o rfSzKoP",
                "item": 79
            }
        },
        {
            "model": "items.Part",
            "pk": 163,
            "fields": {
                "name": "Z XZEL",
                "item": 79
            }
        },
        {
            "model": "items.Part",
            "pk": 164,
            "fields": {
                "name": "gNZs ldmUHSJM IgrRqt",
                "item": 80
            }
        },
        {
            "model": "items.Part",
            "pk": 165,
            "fields": {
                "name": "cpjUPhAs oYC Be LmwvzYS OFbMqwj rXyIgi",
                "item": 81
            }
        },
        {
            "model": "items.Part",
            "pk": 166,
            "fields": {
                "name": "bOIdwRn QUrFCvXo I",
                "item": 81
            }
        },
        {
            "model": "items.Part",
            "pk": 167,
            "fields": {
                "name": "sRD gRIB",
                "item": 82
            }
        },
        {
            "model": "items.Part",
            "pk": 168,
            "fields": {
                "name": "bjQTnf rs WrL",
                "item": 83
            }
        },
        {
            "model": "items.Part",
            "pk": 169,
            "fields": {
                "name": "rMWB bT",
                "item": 83
            }
        },
        {
            "model": "items.Part",
            "pk": 170,
            "fields": {
                "name": "slhXtHC eUDFC zcqZbCO",
                "item": 84
            }
        },
        {
            "model": "items.Part",
            "pk": 171,
            "fields": {
                "name": "YFxARbag rHiSERo oPe xE O",
                "item": 84
            }
        },
        {
            "model": "items.Part",
            "pk": 172,
            "fields": {
                "name": "jr IaeJKVlN lUjGqNJ",
                "item": 85
            }
        },
        {
            "model": "items.Part",
            "pk": 173,
            "fields": {
                "name": "djYZt XoEnhd KwiMcP V xXlFWhK",
                "item": 85
            }
        },
        {
            "model": "items.Part",
            "pk": 174,
            "fields": {
                "name": "wosYNLAx I TtNVJb RTepPJl dVOwvGug D cSlJ",
                "item": 86
            }
        },
        {
            "model": "items.Part",
            "pk": 175,
            "fields": {
                "name": "ZmG jYFasbQy RNTjKf MWk L t uLxBmZaJ",
                "item": 87
            }
        },
        {
            "model": "items.Part",
            "pk": 176,
            "fields": {
                "name": "p",
                "item": 87
            }
        },
        {
            "model": "items.Part",
            "pk": 177,
            "fields": {
                "name": "VTuLzSh ZuhJ",
                "item": 87
            }
        },
        {
            "model": "items.Part",
            "pk": 178,
            "fields": {
                "name": "TmXEges dkbYqoGH",
                "item": 88
            }
        },
        {
            "model": "items.Part",
            "pk": 179,
            "fields": {
                "name": "XVbOhFw OzHY JIfHjY FWpzetyG zHU OPigJCYI f",
                "item": 88
            }
        },
        {
            "model": "items.Part",
            "pk": 180,
            "fields": {
                "name": "EAvUhCId dTF NZewdC EkBYG",
                "item": 88
            }
        },
        {
            "model": "items.Part",
            "pk": 181,
            "fields": {
                "name": "iND MV UOT vE s Lyifw IBNWEOYl",
                "item": 89
            }
        },
        {
            "model": "items.Part",
            "pk": 182,
            "fields": {
                "name": "sCxv SDHp",
                "item": 89
            }
        },
        {
            "model": "items.Part",
            "pk": 183,
            "fields": {
                "name": "PJoRkcx GOLc w FsGRTbC YhHo nLJEebfv",
                "item": 90
            }
        },
        {
            "model": "items.Part",
            "pk": 184,
            "fields": {
                "name": "UvmaMhyw boILBmt noCSvL",
                "item": 91
            }
        },
        {
            "model": "items.Part",
            "pk": 185,
            "fields": {
                "name": "gTJtUC IatOSclg",
                "item": 92
            }
        },
        {
            "model": "items.Part",
            "pk": 186,
            "fields": {
                "name": "kGbzCryp wPXizB ydExilOq",
                "item": 93
            }
        },
        {
            "model": "items.Part",
            "pk": 187,
            "fields": {
                "name": "G Jhqsw iwAl EU DuNS GKnbQB",
                "item": 93
            }
        },
        {
            "model": "items.Part",
            "pk": 188,
            "fields": {
                "name": "voeAr goSPl ojWRfiD am zlA a",
                "item": 94
            }
        },
        {
            "model": "items.Part",
            "pk": 189,
            "fields": {
                "name": "hMuQt FQH kJfmy eMAybYO r ASDnrcg",
                "item": 94
            }
        },
        {
            "model": "items.Part",
            "pk": 190,
            "fields": {
                "name": "nLY gZzqexkt IdTxY EDm GemKOhJ",
                "item": 94
            }
        },
        {
            "model": "items.Part",
            "pk": 191,
            "fields": {
                "name": "cYoLD LEmyAPio hyKexB aVD OJvxtC cbKhRe rVxjfu",
                "item": 95
            }
        },
        {
            "model": "items.Part",
            "pk": 192,
            "fields": {
                "name": "YN Af DElFzMe cmYG azLhCxoy dFsUZSe",
                "item": 95
            }
        },
        {
            "model": "items.Part",
            "pk": 193,
            "fields": {
                "name": "x OLMCXy H NhRYP nBWJtO WT",
                "item": 96
            }
        },
        {
            "model": "items.Part",
            "pk": 194,
            "fields": {
                "name": "fmhEvyN DZWLiYT",
                "item": 96
            }
        },
        {
            "model": "items.Part",
            "pk": 195,
            "fields": {
                "name": "pKhVNvMy RXFZz SIMucoAp Qay doPagzKt",
                "item": 97
            }
        },
        {
            "model": "items.Part",
            "pk": 196,
            "fields": {
                "name": "lfPCiI MhKJday atiJ zOMZm",
                "item": 97
            }
        },
        {
            "model": "items.Part",
            "pk": 197,
            "fields": {
                "name": "sGZ qJa I Thp XmZseUC H sPdxKot",
                "item": 98
            }
        },
        {
            "model": "items.Part",
            "pk": 198,
            "fields": {
                "name": "eXlOkMr kIlLgK EI ClWbmU CUiqtwP",
                "item": 98
            }
        },
        {
            "model": "items.Part",
            "pk": 199,
            "fields": {
                "name": "vCnHKc juNO DhctnYq WyBCdmM",
                "item": 99
            }
        },
        {
            "model": "items.Part",
            "pk": 200,
            "fields": {
                "name": "LYel EAptN ZWyxiG P",
                "item": 100
            }
        }
    ]
    ' > data.json

    python manage.py loaddata data.json
  SHELL
end
