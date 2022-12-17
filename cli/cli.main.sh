#this is program in directory cliapp
#../Baphomate-AI/cli/cli.main.sh
main(){
    #..color/warna
    red="\033[1;31m" #/kebaya merah
    grn="\033[1;32m" #/warna kesukaan aing
    ylw="\033[1;33m" #/warna caduk
    blu="\033[1;34m" #/viking nih bosss 
    pop="\033[1;35m" #/janda syemock rasa perawan
    cyn="\033[1;36m" #/warna langit cerah secerah hatiku anjay serepetetetetett
    def="\033[0m" #/bawaan
    clear
    menu(){
        echo -e """
            
        $def  +--------------------------+
        $red┌─$def|$cyn     Baphomate CLI App$def    |
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
        $red├──•$def 1. Materi
        $red├──•$def 2. Tolkit 
        $red│
        $red└──╼•$def 0.Back
        """        
    }
    menu
    read -p "[#]Bap/CliApp> " cli;
    if [[ $cli == 1 ]]; then #../materi
        python cli/materi/main.materi.py 
    elif [[ $cli == 2 ]]; then #..tolkit
        echo -e "$ylw(?) This program is currently being developed$def"
        read -p "[ENTER TO BACK]"
        bash cli/cli.main.sh
    elif [[ $cli == 0 ]]; then #../back
        bash main.sh
    else
        echo -e "$red (!)Wrong input "
        sleep 2
        bash cli/cli.main.sh
    fi    
    #..DONE            
}
main
