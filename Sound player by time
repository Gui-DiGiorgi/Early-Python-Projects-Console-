# This player has 3 functions, the first is to play all the songs of the 
# playlist in an infinite loop, another is to play an specific number of 
# songs, and the last is to play during an specific time, calculated by 
# how certain songs fit about that time. Once the mode has been chosen, 
# you can only choose another mode by closing and opening the script.

# The folder input and output are folders where the sound files are 
# located, put your mp3 files on the input folder and the script will 
# make wave files for the output folder, and those will be used by the 
# script.

# The language of the interface is portuguese

import wave, pyaudio, time
import contextlib
import random
import os, sys

# Conversor .mp3 pra .wav

def file_organizer():
    from pydub import AudioSegment
    
    location=os.path.dirname(os.path.abspath(__file__))
        
    os.chdir(location)
        
    file_list=os.listdir(location+"\\input")
    
    mp3=[]
    
    for i in file_list:
        if i[-4::1]==".mp3":
            mp3+=[i]
    wave=[]
    
    file_list=os.listdir(location+"\\output")
    
    for i in file_list:
        if i[-4::1]==".wav":
            wave+=[i]
            
    fake_waves=[]
            
    for mp in mp3:
        fake_wave=mp[0:-4]+".wav"
        if fake_wave not in wave:
            fake_waves+=[mp]
    
    fake_mp3s=[]
    
    for wa in wave:
        fake_mp3=wa[0:-4]+".mp3"
        if fake_mp3 not in mp3:
            fake_mp3s+=[wa]
    
    for fmp in fake_mp3s:
        os.remove(location+"\\output\\"+fmp)
        
    for fwa in fake_waves:
        # files
        song_i = ("input/"+fwa)
        new_song=fwa[0:-4]
        song_o = ("output/"+new_song+".wav")
        
        # convert mp3 to wav                                                            
        sound = AudioSegment.from_mp3(song_i)
        sound.export(song_o, format="wav")

def clearer(a):
    clear=""
    for i in range(len(a)+1):
        clear+=" "
    print(clear,end="\r")

def hour_set():
    
    import time
    
    true_time=time.localtime()
    
    print("\nAgora são "+str(true_time[3])+" hora(s) e "+str(true_time[4])+" minutos.\nDefina o horário limite:\n")
    
    set_time=["Hora (de 0 até 23): ","Minutos (de 0 até 59): "]
    
    for n in range(len(set_time)):
        set_time[n]=int(input(set_time[n]))
        
    true_time=time.localtime()
        
    if (set_time[0]<true_time[3] or (set_time[0]==true_time[3] and set_time[1]<true_time[4])):
        true_time=time.localtime(time.time()+60*60*24)
        
    new_time=[]
    
    for i in true_time:
        new_time.append(i)
    
    new_time[3]=set_time[0]
    new_time[4]=set_time[1]
    
    newest_time=tuple(new_time)
    
    remaining_time=round(time.mktime(newest_time)-time.time(),1)
    
    return remaining_time

file_organizer()

mode=int(input("Você quer ouvir música: 0.Em loop infinito? 1.Por número de músicas? 2.Por tempo? \nDigite sua escolha. "))

while not (mode==0 or mode==1 or mode==2):
    print("Digite uma escolha válida")
    mode=int(input("\nComo quer ouvir música: 0.Loop infinito 1.Por número de músicas? 2.Por tempo? "))

exit=0

next_song_const=3

location=os.path.dirname(os.path.abspath(__file__))
    
os.chdir(location)
    
music_list=os.listdir(location+"\\output")

while mode==0:

	if exit==0:
		print()
		exit=1
		start_time=time.time()

    loop=0
    r_song=random.randint(0,len(music_list)-1)
    song_name=music_list[r_song][0:-4]
    sname = ('output/'+music_list[r_song])
    with contextlib.closing(wave.open(sname,'r')) as f:
        frames = f.getnframes()
        rate = f.getframerate()
        duration = frames / float(rate)
        duration=int(duration)
    
    sound = wave.open(sname)
    p = pyaudio.PyAudio()
    chunk = 1024
    stream = p.open(format =
                    p.get_format_from_width(sound.getsampwidth()),
                    channels = sound.getnchannels(),
                    rate = sound.getframerate(),
                    output = True)
    data = sound.readframes(chunk)
    b=time.time()
    while (time.time()-b)<duration:
        stream.write(data)
        data = sound.readframes(chunk)
        text="Música: "+song_name+ "  -  Tempo: "+"{0:.2f}".format(time.time()-b)+"/"+str(duration)+"s  -  Loop: "+str(loop)+"  -  Tempo total: "+"{0:.2f}".format((time.time()-start_time)/60)+" min"
        print(text,end="\r")

    music_list.remove(music_list[r_song])

    clearer(text)

    next_song=next_song_const

    for i in range(next_song):
        print("Próxima música em "+str(next_song),end="\r")
        next_song-=1
        time.sleep(1)

    if music_list==[]:
        music_list=os.listdir(location+"\\output")
        loop+=1

while mode==1 and type(exit)==int:

    n_songs=int(input("\nQuantas músicas você quer? "))

    while n_songs>len(music_list):
    	print("\nPor favor, escolha um número menor que {}.".format(len(music_list)+1))
    	n_songs=int(input("Quantas músicas você quer? "))

    print()
    n=0
    c_songs=[]
    
    while n<n_songs and type(exit)==int:

        r_song=random.randint(0,len(music_list)-1)
        song_name=music_list[r_song][0:-4]
        c_songs+=[song_name]
        sname = ('output/'+music_list[r_song])
        with contextlib.closing(wave.open(sname,'r')) as f:
            frames = f.getnframes()
            rate = f.getframerate()
            duration = frames / float(rate)
            duration=int(duration)
        
        sound = wave.open(sname)
        p = pyaudio.PyAudio()
        chunk = 1024
        stream = p.open(format =
                        p.get_format_from_width(sound.getsampwidth()),
                        channels = sound.getnchannels(),
                        rate = sound.getframerate(),
                        output = True)
        data = sound.readframes(chunk)
        b=time.time()
        while (time.time()-b)<duration:
            stream.write(data)
            data = sound.readframes(chunk)
            text="Música: "+song_name+ " ("+str(n+1)+"/"+str(n_songs)+")" + "  -  Tempo: "+"{0:.2f}".format(time.time()-b)+"/"+str(duration)+"s"
            print(text,end="\r")

        music_list.remove(music_list[r_song])

        clearer(text)

        n+=1
        if n<n_songs:
            next_song=next_song_const
            for i in range(next_song):
                print("Próxima música em "+str(next_song),end="\r")
                next_song-=1
                time.sleep(1)
        if n==n_songs:
            print("\nEssas foram as",n,"músicas:")

            print()

            neat_list=0

            for played_song in c_songs:
                neat_list+=len(played_song)
                if neat_list>60:
                    neat_list=0
                    print()
                if c_songs.index(played_song)!=len(c_songs)-1:
                    print(played_song,end=", ")
                else:
                    print(played_song)


            exit=input("\nAperte ENTER para sair ou digite o novo número de músicas para tocar: ")
            try:
                if type(int(exit))==int and int(exit)>=1:
                    music_list=os.listdir(location+"\\output")
                    exit=int(exit)
                    while exit>len(music_list):
                        print("Por favor, escolha um número menor que {}.".format(len(music_list)+1))
                        exit=int(input("\nQuantas músicas você quer? "))
                    print()
                    n_songs=exit
                    n=0
                    c_songs=[]                      
            except:
                print("Obrigado por usar esse programa, tchau!")
                time.sleep(next_song_const)

while mode==2 and type(exit)==int:

	sub_mode=int(input("Você quer escutar música: 1.Por certos minutos? 2.Até certo horário? \nDigite sua escolha. "))

	while not (sub_mode==1 or sub_mode==2):
    	print("Digite uma escolha válida")
    	sub_mode=int(input("\nComo quer ouvir música: 1.Por certos minutos? 2.Até certo horário? "))

    music_list=os.listdir(location+"\\output")
    
    chosen_music_list=[]
    duration_list=[]
    
    for name in music_list:
        file = ('output/'+name)
        with contextlib.closing(wave.open(file,'r')) as f:
            frames = f.getnframes()
            rate = f.getframerate()
            duration = frames / float(rate)
            duration=int(duration)
            duration_list+=[[duration,name]]
    
    av=0
    
    for i in duration_list:
        av+=i[0]
        
    av/=len(music_list)
        
    limit_time=3*(av+next_song_const)

    if sub_mode==1:
    
    	chosen_time=round(float(input("\nQuantos minutos? ")),1)*60
    	current_chosen_time=chosen_time
    
    	while chosen_time<av or chosen_time>av*len(music_list)/2:
        	print("Por favor, escolha um número entre {0} e {1}.".format(round(av/60,1),round(av*len(music_list)/120,1)))
        	chosen_time=round(float(input("\nQuantos minutos? ")),1)*60
        	current_chosen_time=chosen_time

	else:

		chosen_time=hour_set()
    	current_chosen_time=chosen_time

    	while chosen_time<av or chosen_time>av*len(music_list)/2:
        	print("Por favor, escolha um horário dentro de {0} e {1} minutos.".format(round(av/60,1),round(av*len(music_list)/120,1)))
        	chosen_time=hour_set()
        	current_chosen_time=chosen_time

    print()
    
    while current_chosen_time>limit_time:
        song_n=random.randint(0,len(duration_list)-1)
        d=duration_list
        current_chosen_time-=(d[song_n][0]+next_song_const)
        chosen_music_list+=[d[song_n][1]]
        duration_list.remove(d[song_n])
        
    if current_chosen_time<limit_time:
        limit_time=current_chosen_time
    
    av=0
    
    for i in duration_list:
        av+=i[0]
        
    av/=len(duration_list)
            
    l=h=av
    
    for i in duration_list:
        if i[0]<l:
            l=i[0]
        if i[0]>h:
            h=i[0]
            
    l=(l//5)*5
    
    h=(h//5+1)*5
    
    tiers=[]
    
    while l<h:
        tiers+=[[l,l+30]]
        l+=30
    
    valid_m1=[]
    
    for i in tiers:
        valid_m1+=[[(i[0]+i[1])/2,0,0,[]]]
        
    for pair in duration_list:
        for i,j in zip(tiers,valid_m1):
            if pair[0]>=i[0] and pair[0]<i[1]:
                j[1]+=1
                j[2]+=100/len(duration_list)
                j[3]+=[pair[1]]
                break
    
    for i in valid_m1:
        i[2]=round(i[2],1)
        
    kill=[]
    
    for i in valid_m1:
        if i[1]*i[0]<limit_time or i[1]<limit_time/(av+next_song_const):
            kill+=[i]
            
    for i in kill:
        valid_m1.remove(i)
        
    #________________________________________________________________________________________________________________________________
    
    system=[]
    
    for i in valid_m1:
        system.append(int(limit_time/(i[0])))
    
    system_v2=[]
    
    for i in system:
        system_v2.append(0)
        
    max_p=0
    max_p_m=[]
    time_error=5
    
    while max_p_m==[]:
        while system_v2!=system:
            for i in range(len(system_v2)):
                if system_v2[i]==system[i]+1:
                    system_v2[i]=0
                    system_v2[i+1]+=1
                            
            #points
            time=0
            t_p=0
            
            for i,j in zip(valid_m1,system_v2):
                time+=(i[0]+next_song_const)*j
                if time>limit_time+time_error:
                    break
            if time<limit_time+time_error and time>limit_time-time_error:
                for i,j in zip(system_v2,valid_m1):
                    t_p+=i*j[2]
                if t_p>max_p:
                    max_p=t_p
                    max_p_m=system_v2.copy()      
            system_v2[0]+=1
            
        if max_p_m==[]:
            time_error+=5
            system_v2=[]
            for i in system:
                system_v2.append(0)
            
    for m,n in zip(max_p_m,range(len(max_p_m))):
        for i in range(m):
            m_choice=random.randint(0,len(valid_m1[n][3])-1)
            song=valid_m1[n][3][m_choice]
            chosen_music_list+=[song]
            valid_m1[n][3].remove(song)
    
    import time
    
    ending=time.time()+chosen_time

    random.shuffle(chosen_music_list)
    
    for chosen_song in chosen_music_list:
    
        song_file = ('output/'+chosen_song)
        with contextlib.closing(wave.open(song_file,'r')) as f:
            frames = f.getnframes()
            rate = f.getframerate()
            duration = frames / float(rate)
            duration=int(duration)
        
        sound = wave.open(song_file)
        p = pyaudio.PyAudio()
        chunk = 1024
        stream = p.open(format =
                        p.get_format_from_width(sound.getsampwidth()),
                        channels = sound.getnchannels(),
                        rate = sound.getframerate(),
                        output = True)
        data = sound.readframes(chunk)
        b=time.time()
        while (time.time()-b)<duration:
            stream.write(data)
            data = sound.readframes(chunk)
            text="Música: "+chosen_song[0:-4]+ " -  Tempo (Música): "+"{0:.2f}".format(time.time()-b)+"/"+str(duration)+"s - Tempo restante: "+"{0:.2f}".format((ending-time.time())/60)+" min"
            print(text,end="\r")
            
        clearer(text)
        
        if chosen_music_list.index(chosen_song)!=len(chosen_music_list)-1:
            next_song=next_song_const
            for i in range(next_song):
                print("Próxima música em "+str(next_song),end="\r")
                next_song-=1
                time.sleep(1)
    
    print("\nEssas foram as",len(chosen_music_list),"músicas: ")
    
    print()
    
    neat_list=0
    
    for chosen_song in chosen_music_list:
        neat_list+=len(chosen_song[0:-4])
        if neat_list>60:
            neat_list=0
            print()
        if chosen_music_list.index(chosen_song)!=len(chosen_music_list)-1:
            print(chosen_song[0:-4],end=", ")
        else:
            print(chosen_song[0:-4])
    
    exit=input("\nAperte ENTER para sair ou digite um número para continuar: ")
    try:
        if type(int(exit))==int:
            exit=int(exit)
            
    except:
        print("Obrigado por usar esse programa, tchau!")
        time.sleep(next_song_const)


