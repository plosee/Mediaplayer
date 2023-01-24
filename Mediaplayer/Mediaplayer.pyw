from import_modules import *
# tkinter windows optins
root = Tk()
root.title("jukebox")
__filepath__ =  str(__file__)
root.iconbitmap(Path(__file__).parent / 'favicon.ico')

def URLoption():
    nupp.grid_forget()
    
    URLentry = Entry(root)
    URLentry.grid(row=0,column=1,sticky=N,padx=10,pady=5)
    
    def entry2():
        URLget = URLentry.get()

        nowplaying = Label(root,text=f'Nüüd mängib: {URLget}')
        nowplaying.grid(row=2,column=1)

        fileW = Path(__file__).parent
        
        VideoSearch = VideosSearch(URLget, limit = 1)
        result = VideoSearch.result()
        id = result["result"][0]["id"]

        plastic = f'https://www.youtube.com/watch?v={id}'
        
        cachepath = fileW / 'media_cache'
        cachepath.mkdir(exist_ok=True)

        yttitle = YouTube(plastic).title
        mp4fail = yttitle + '.mp4'
        oggfail = yttitle + '.ogg'
        oggpath = cachepath / oggfail
        mp4path = Path(cachepath / mp4fail)

        if mp4path.exists() == False:
            audioyt = YouTube(plastic).streams.filter(only_audio=True).first()
            mp4path = audioyt.download(output_path=cachepath)
            
        newpath = Path(os.path.join(cachepath, mp4fail))

        if not newpath.exists():
            os.rename(mp4path, newpath)

        if not oggpath.exists():
            b = subprocess.run([
            'ffmpeg', '-i', os.path.join(cachepath, mp4fail), 
            '-c:a', 'libvorbis', '-q:a', '4',
            os.path.join(cachepath, oggfail) 
            ])

        mixer.init()
        
        try:
            mixer.music.load(oggpath)
        except Exception as eror:
            if eror == 'pygame.error: Not an Ogg Vorbis audio stream':
                tkinter.messagebox.showerror('Error', 
                'Palun kustutage .ogg fail, eelmises sessionis script ei suutnud seda teha. Et seda ei juhtuks uuesti, palun lopetage muusika kuulamine enne sessiooni lopetamist.')
            else:
                quit()
                
        mixer.music.play()
        
        URLentry.grid_forget()
        option2.grid_forget()


        def ruudud():
            mixer.music.stop()
            nowplaying.grid_forget()
            nupp3.grid_forget()
            openmenu()

        nupp3 = Button(root, text = 'Tagasi', command=ruudud)
        nupp3.grid(row=4,column=1, pady=5)
        
    option2.config(text="vajuta siia kui loo nimi on valitud", command=entry2)
    
def loendid():
    global rlist
    global loend
    nupp.grid_forget()
    option2.grid_forget()
    # uses filedialog so the user can select a file containing the file which has song titles in   
    faili_tyyp = [("Teksti failid (.txt)", ".txt")]
    nimi = filedialog.askopenfile(filetypes=faili_tyyp)
    valik = nimi.readlines()

    loend = ""
    list = ""
    arv = 0
    #appends titles into list        
    for i in valik:
        arv += 1
        loend += f' {arv}. {i} '
        list += i
    rlist = list.split('\n')

    # print(list)
    menu()

def menu():

    nupp.config(text="Restart sellest nupust kui soovid lauluvalikut vahetada", command = openmenu)
    nupp.grid(row=0, column=1,sticky=N,padx=10, pady=5)
    sisu = Label(root,text=f'=======================\n{loend}\n=======================')
    sisu.grid(row=1,column=1)
      
    kysimus = Label(root, text='mis lugu soovite mangida?\nLugu saab valida järjekorranumbriga.')
    kysimus.grid(row=2,column=1)

    lauluvalik = Entry(root)
    lauluvalik.grid(row=3,column=1)
    
    def entry():
        # just for errors if entryget is not integer or above the list ints
        try:
            vastus = int(lauluvalik.get())
        except ValueError:
            tkinter.messagebox.showerror(
                'Error', 'Palun valige kasutatav number jarjekorrast.')  
            menu()

        vastus -= 1
        
        urlsearch = rlist[vastus]

        kysimus.grid_forget()
        lauluvalik.grid_forget()
        nupp.grid_forget()
        nupp2.grid_forget()

        try:
            nowplaying = Label(root,text=f'Nüüd mängib: {rlist[vastus]}')
            nowplaying.grid(row=2,column=1)
        except IndexError:
            tkinter.messagebox.showerror('Error', 'See number on jarjekorrast valjas, palun valige jarjekorras olev number')
            menu()

        fileW = Path(__file__).parent

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
            mp4path = audioyt.download(output_path=cachepath)
            # print('if audio download tootas')
            
        # print(mp4path.exists())
        # print(oggpath.exists())
        # print(mp4path)
        # print(oggpath)

        newfilename = str(urlsearch + '.mp4') 
        newpath = Path(os.path.join(cachepath, newfilename))

        # print(type(newfilename))
        # print(type(cachepath))

        if not newpath.exists():
            os.rename(mp4path, newpath)

        if not oggpath.exists():
            b = subprocess.run([
            'ffmpeg', '-i', os.path.join(cachepath, newfilename), 
            '-c:a', 'libvorbis', '-q:a', '4',
            os.path.join(cachepath, oggfail) 
            ])
        # else:
        #     print('ffmpeg if ja elif skipiti')

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
            nowplaying.grid_forget()
            nupp3.grid_forget()
            nupp.grid_forget
            kysimus.grid_forget()
            sisu.grid_forget()
            lauluvalik.grid_forget()
            mixer.music.stop()
            openmenu()

        nupp3 = Button(root, text = 'Tagasi', command=ruudud)
        nupp3.grid(row=4,column=1, pady=5)

    nupp2=Button(root, text = 'Mängi!', command=entry)
    nupp2.grid(row=4,column=1, pady=5)

def openmenu():
    global nupp
    global option2
    
    nupp=Button(root, text = "Vajuta siia et muusikavalikut kuvada!", command = loendid)
    nupp.grid(row=0, column=1,sticky=N,padx=10, pady=5,)

    option2 = Button(root, text = "Vajuta siia, et mangida laulu URList!", command = URLoption)
    option2.grid(row=1, column=1,sticky=N,padx=10,pady=5,)
    
openmenu()

def delete_file(name):
    shutil.rmtree(Path(name))
    
fileA = ""
fileA += __file__
fileKAKA = fileA.replace('Mediaplayer.py', '')
kaka = str(Path(fileKAKA) / 'media_cache')

atexit.register(delete_file, kaka)

root.mainloop()