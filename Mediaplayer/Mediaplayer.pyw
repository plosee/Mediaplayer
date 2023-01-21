from import_modules import *

aken = Tk()
aken.title("jukebox")
__filepath__ =  str(__file__)
aken.iconbitmap(Path(__file__).parent / 'favicon.ico')

def loendid():
    global rlist
    global loend

    nupp.grid_forget()

    faili_tyyp = [("Teksti failid (.txt)", ".txt")]
    nimi = filedialog.askopenfile(filetypes=faili_tyyp)
    valik = nimi.readlines()

    loend = ""
    list = ""
    arv = 0

    for i in valik:
        arv += 1
        loend += f' {arv}. {i} '
        list += i
    rlist = list.split('\n')

    print(list)
    menu()

def menu():

    nupp.config(text="Restart sellest nupust kui soovid lauluvalikut vahetada", command=loendid)
    nupp.grid(row=0, column=1,sticky=N,padx=10, pady=5)
    sisu = Label(aken,text=f'=======================\n{loend}\n=======================').grid(row=1,column=1)
      
    kysimus = Label(aken, text='mis lugu soovite mangida?\nLugu saab valida järjekorranumbriga.')
    kysimus.grid(row=2,column=1)

    lauluvalik = Entry(aken)
    lauluvalik.grid(row=3,column=1)

    def entry():
        try:
            vastus = int(lauluvalik.get())
        except ValueError:
            tkinter.messagebox.showerror(
                'Error', 'Palun valige kasutatav number jarjekorrast.')  
            menu()

        vastus -= 1

        kysimus.grid_forget()
        lauluvalik.grid_forget()
        nupp.grid_forget()
        nupp2.grid_forget()

        try:
            nowplaying = Label(aken,text=f'Nüüd mängib: {rlist[vastus]}')
            nowplaying.grid(row=2,column=1)
        except IndexError:
            tkinter.messagebox.showerror('Error', 'See number on jarjekorrast valjas, palun valige jarjekorras olev number')
            menu()

        fileW = ""
        fileW += __file__
        fileW = Path(fileW).parent

        urlsearch = rlist[vastus]

        VideoSearch = VideosSearch(urlsearch, limit = 1)
        result = VideoSearch.result()
        id = result["result"][0]["id"]

        plastic = f'https://www.youtube.com/watch?v={id}'
        
        cachepath = fileW / 'media_cache'
        cachepath.mkdir(exist_ok=True)

        yttitle = YouTube(plastic).title
        mp4fail = yttitle + '.mp4'
        oggfail = urlsearch + '.ogg'
        oggpath = cachepath / oggfail
        stroggpath = str(cachepath / oggfail)
        mp4path = Path(cachepath / mp4fail)

        if mp4path.exists() == False:
            audioyt = YouTube(plastic).streams.filter(only_audio=True).first()
            out_file = audioyt.download(output_path=cachepath)
            # print('if audio download tootas')
        else:
            out_file = Path(cachepath / mp4fail)

        mp4path = Path(out_file)

        # print(mp4path.exists())
        # print(oggpath.exists())
        # print(mp4path)
        # print(oggpath)

        newfilename = str(urlsearch + '.mp4') 
        newpath = os.path.join(cachepath, newfilename)

        # print(type(newfilename))
        # print(type(cachepath))

        os.rename(mp4path, newpath)

        if oggpath.exists() == False:
            b = subprocess.run([
            'ffmpeg', '-i', os.path.join(cachepath, newfilename), 
            '-c:a', 'libvorbis', '-q:a', '4',
            os.path.join(cachepath, oggfail) 
            ])
        else:
            print('ffmpeg if ja elif skipiti')
            pass

        mixer.init()
        try:
            mixer.music.load(stroggpath)
        except Exception as eror:
            if eror == 'pygame.error: Not an Ogg Vorbis audio stream':
                tkinter.messagebox.showerror('Error', 
                'Palun kustutage .ogg fail, eelmises sessionis script ei suutnud seda teha. Et seda ei juhtuks uuesti, palun lopetage muusika kuulamine enne sessiooni lopetamist.')
            else:
                # print(eror)
                # print('Unknown error')
                quit()
        mixer.music.play()

        def ruudud():
            nupp.grid(row=0, column=1,sticky=N,padx=10, pady=5,)
            nowplaying.grid_forget()
            nupp3.grid_forget()
            mixer.music.stop()
            menu()

        nupp3 = Button(aken, text = 'Tagasi', command=ruudud)
        nupp3.grid(row=4,column=1, pady=5)

    nupp2=Button(aken, text = 'Mängi!', command=entry)
    nupp2.grid(row=4,column=1, pady=5)

nupp=Button(aken, text = "Vajuta siia et muusikavalikut kuvada!", command = loendid)
nupp.grid(row=0, column=1,sticky=N,padx=10, pady=5,)

def delete_file(name):
    shutil.rmtree(Path(name))
    
fileA = ""
fileA += __file__
fileKAKA = fileA.replace('Mediaplayer.py', '')
kaka = str(Path(fileKAKA) / 'media_cache')

atexit.register(delete_file, kaka)

aken.mainloop()