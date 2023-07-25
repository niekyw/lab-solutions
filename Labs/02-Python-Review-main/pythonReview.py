
# 2
def create_youtube_video(title, description, hashtag = None):
    vid = {'title': title,
            'description': description,
            'likes': 0,
            'dislikes': 0,
            'comments': {}}

    # how to ensure up to 5 words? how to ensure no duplicates?
    if hashtag is not None:
        hashtag = list(set(hashtag))
        vid['hashtag'] = hashtag[:5]
        
    return vid
#3
def like(vid):
    if 'likes' in vid:
        vid['likes'] += 1
    return vid

#4
def dislike(vid):
    if 'dislikes' in vid:
        vid['dislikes'] += 1
    return vid

#5
### change to list to accommodate multiple comments
def add_comment(vid, username, comment):
    vid_comments = vid['comments']
    vid['comments'][username] = comment
    return vid

#bonus
def similarity_to_video(vid1, vid2):
    if 'hashtag' in vid1:
        hashtags1 = set(vid1['hashtag'])
    else:
        hashtags1 = set()
    if 'hashtag' in vid2:
        hashtags2 = set(vid2['hashtag'])
    else:
        hashtags2 = set()
    return len(set.intersection(hashtags1, hashtags2)) / max(len(hashtags1), len(hashtags2))

#6
vid = create_youtube_video('MEET 101', 'How to Have Fun in Meet')
for i in range(495):
    like(vid)
#print(vid)


#bonus
hashtags1 = ['meet', 'fun', 'summer', 'cs', 'unfun']
hashtags2 = ['meet', 'fun', 'entrep', 'cs', 'learn']
vid1 = create_youtube_video('MEET 101', 'How to Have Fun in Meet', hashtags1)
vid2 = create_youtube_video('MEET 101', 'How to Have Fun in Meet', hashtags2)
print(similarity_to_video(vid1, vid2))
