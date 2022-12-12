#!/bin/bash
#/created on 12/12/2022 by kirasinigami & 4yourpage
#/lisence: CC0 1.0 Universal
#/package: npmjs for web scanner
clear
main(){
    #..color/warna
    red="\033[1;31m" #/kebaya merah
    grn="\033[1;32m" #/warna kesukaan aing
    ylw="\033[1;33m" #/warna caduk
    blu="\033[1;34m" #/viking nih bosss 
    pop="\033[1;35m" #/janda syemock rasa perawan
    cyn="\033[1;36m" #/warna langit cerah secerah hatiku anjay serepetetetetett
    def="\033[0m" #/bawaan
    
    #.../packages installer
    install(){
        clear
        echo -e "$ylw [*] Installing packages..."
        sleep 2
        pkg update -y && pkg upgrade -y
        pkg install -y python 
        pip install requets 
        bash main.sh
    } #../done installer
    #..webapp
    webapp(){
        clear
        echo -e """
            
            
        $def  +--------------------------+
        $red┌─$def|$cyn    Welcole To WEBAPP$def     |
        $red│$def +--------------------------+
        $red│
        $red├──$def • Author     :$grn Kirasinigami 
        $red├──$def • Contributor:$grn 4Yourpage 
        $red├──$def • Project    :$ylw Baphomate AI 
        $red├──$def • Version    :$red 1.0.1$def stable CLI 
        $red├──$def • Lisence    :$ded CCO 1.0 Universal 
        $red├────────────────────────────────────•
        $red│
        $red├──[$def MENU WEBAPP$red ]
        $red│
        $red├──•$def 1. Web Scanner QR code 
        $red├──•$def 2. Web Cam test (coming soon)
        $red│
        $red└──╼•$def 0.back 
        
        """
    }
    #...banner/baliho & menu
    banner(){
        echo -e """
            
        $def  +--------------------------+
        $red┌─$def|$cyn  Welcole To Baphomate AI$def |
        $red│$def +--------------------------+
        $red│
        $red├──$def • Author     :$grn Kirasinigami 
        $red├──$def • Contributor:$grn 4Yourpage 
        $red├──$def • Project    :$ylw Baphomate AI 
        $red├──$def • Version    :$red 1.0.1$def stable CLI 
        $red├──$def • Lisence    :$ded CCO 1.0 Universal 
        $red├────────────────────────────────────•
        $red│
        $red├──[$def HOME MENU$red ]
        $red│
        $red├──•$def 1. Install packages (recomend)
        $red├──•$def 2. WEB APP 
        $red├──•$def 3. CLI APP 
        $red├──•$def 4. Update 
        $red├──•$def 5. Report 
        $red├──•$def 6. Join forums 
        $red│
        $red└──╼•$def 0.Exit  
        """
    }
    banner
    read -p "[#]Bap> " c; #../shell cmd
    #../logic
    if [[ $c == 1 ]]; then 
        install
    elif [[ $c == 2 ]]; then
        webapp
        read -p "[#]Bap/Webapp> " web; #../shell cmd webapp
        if [[ $web == 1 ]]; then
           echo -e "$grn[*] Setup webapp..."
           sleep 1
           echo -e "$grn[*] Running server ..."
           sleep 2 
           echo -e """
           +---------------------------------+
           | Server running by python server |
           +---------------------------------+
           host: localhost
           port: 8080
           link: http://localhost:8080/web/BaphomateSCANNER/
           ____________________________________
           note: copy the link localhost and paste it in the browser
           CTRL + c to stop 
           """
           python -m http.server 8080
           bash main.sh
        elif [[ $web == 2 ]]; then 
            echo -e "$ylw(?) This program is currently being developed$def"
            read -p "[ENTER TO BACK]"
            bash main.sh
        elif [[ $web == 0 ]]; then
            bash main.sh
        else
            echo -e "$red (!)Wrong input "
            sleep 2
            bash main.sh
        fi #../done
        
    elif [[ $c == 3 ]]; then
        echo -e "$ylw(?) This program is currently being developed$def"
        read -p "[ENTER TO BACK]"
        bash main.sh
    elif [[ $c == 4 ]]; then 
        git pull 
    elif [[ $c == 5 ]]; then 
        xdg-open https://wa.me/+6285759669252
        sleep 1
        bash main.sh
    elif [[ $c == 6 ]]; then 
        xdg-open https://forums.baphomate.rf.gd
        bash main.sh
    elif [[ $c == 0 ]]; then
        clear
        sleep 1
        echo -e "$ylw Thank you for interacting on Baphomate.AI"
        sleep 2 
        xdg-open https://baphomate.rf.gd
        exit
    else
        echo -e "$red (!)Wrong input "
        sleep 2
        bash main.sh
    fi    
    #..DONE    
}
main