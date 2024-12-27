from django.shortcuts import render, redirect, get_object_or_404
from .models import Track


def home_page(request):
    return render(request, 'index.html')

def music_list(request):
    tracks = Track.objects.all()
    ctx = {'tracks': tracks}
    return render(request, 'tracks/music-list.html', ctx)

def music_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        artist = request.POST.get('artist')
        album = request.POST.get('album')
        genre = request.POST.get('genre')
        release_date = request.POST.get('release-date')
        cover_image = request.FILES.get('cover-image')
        audio_file = request.FILES.get('audio-file')
        if title and artist and album and genre and release_date and cover_image and audio_file:
            Track.objects.create(
                title=title,
                artist=artist,
                album=album,
                genre=genre,
                release_date=release_date,
                cover_image=cover_image,
                audio_file=audio_file
            )
            return redirect('tracks:music-list')
    return render(request, 'tracks/music-create.html')

def music_detail(request, track_id):
    track = get_object_or_404(Track, pk=track_id)
    ctx = {'track':track}
    return render(request, 'tracks/music-detail.html', ctx)

def music_update(request, track_id):
    track = get_object_or_404(Track, pk=track_id)
    if request.method == 'POST':
        title = request.POST.get('title')
        artist = request.POST.get('artist')
        album = request.POST.get('album')
        genre = request.POST.get('genre')
        release_date = request.POST.get('release-date')
        cover_image = request.FILES.get('cover-image')
        audio_file = request.FILES.get('audio-file')
        if title and artist and album and genre and release_date and cover_image and audio_file:
            track.title = title
            track.artist = artist
            track.album = album
            track.genre = genre
            track.release_date = release_date
            track.cover_image = cover_image
            track.audio_file = audio_file
            track.save()
            return redirect('tracks:music-detail', track_id=track.id)
    ctx = {'track':track}
    return render(request, 'tracks/music-update.html', ctx)

def music_delete(request, track_id):
    track = get_object_or_404(Track, pk=track_id)
    if request.method == 'POST':
        track.delete()
        return redirect('tracks:music-list')
    ctx = {'track': track}
    return render(request, 'tracks/music-delete-confirm.html', ctx)