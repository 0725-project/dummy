import requests

base_url = 'http://localhost:3000/api'

def api_call(endpoint, method='GET', data=None, headers=None):
    url = f'{base_url}/{endpoint}'

    if method == 'GET':
        response = requests.get(url, headers=headers)
    elif method == 'POST':
        response = requests.post(url, json=data, headers=headers)
    elif method == 'PUT':
        response = requests.put(url, json=data, headers=headers)
    elif method == 'DELETE':
        response = requests.delete(url, headers=headers)
    else:
        raise ValueError('Invalid HTTP method')

    response.raise_for_status()

    print(f'API Call: {method} {url} => {response.status_code}')
    if not response.content:
        return {}
    return response.json()

if __name__ == '__main__':
    try:
        api_call('health')
    except Exception as e:
        print(f'Error occurred: {e}')
        exit(1)

    # dummy users
    def create_dummy_user(username, nickname, password, email, description):
        user_data = {
            'username': username,
            'nickname': nickname,
            'password': password,
            'email': email,
            'description': description
        }
        create_user_response = api_call('auth/register', method='POST', data=user_data)

        auth_data = {
            'username': username,
            'password': password
        }
        auth_login_response = api_call('auth/login', method='POST', data=auth_data)
        access_token = auth_login_response.get('accessToken')

        return {
            'id': create_user_response.get('id'),
            'username': create_user_response.get('username'),
            'response': create_user_response,
            'accessToken': access_token 
        }

    user_foo_response = create_dummy_user('foo', 'Kim Jun Young', 'securePassword1234@', 'normal8781@gmail.com', 'Hello, I am a software developer.')
    user_john_response = create_dummy_user('john', 'John Mayer', 'q1w2e3r4!@', 'john.mayer@example.com', 'Hello, I am a musician.')
    user_trump_response = create_dummy_user('trump', 'Donald Trump', 'trump2024!@', 'donald.trump@example.com', 'Hello, I am a businessman.')
    user_elon_response = create_dummy_user('elon', 'Elon Musk', 'spacex2024!@', 'elon.musk@example.com', 'Hello, I am an entrepreneur.')
    user_james_response = create_dummy_user('james', 'James Bond', '007!@', 'james.bond@example.com', 'Hello, I am a secret agent.')
    user_eminem_response = create_dummy_user('eminem', 'Eminem', 'rapGod2024!@', 'eminem@example.com', 'Hello, I am a rapper.')
    user_freddie_response = create_dummy_user('freddie', 'Freddie Mercury', 'queen1946!@', 'freddie.mercury@example.com', 'Hello, I am a frontman.')
    user_bar_response = create_dummy_user('bar', 'Barack Obama', 'yeswecan2024!@', 'barack.obama@example.com', 'Hello, I am a former president.')

    # dummy topics
    def create_dummy_topic(topicSlug, topicName, description, user):
        topic_data = {
            'topicSlug': topicSlug,
            'topicName': topicName,
            'description': description
        }
        headers = {
            'Authorization': f'Bearer {user['accessToken']}'
        }
        create_topic_response = api_call('topics', method='POST', data=topic_data, headers=headers)
        topic_id = create_topic_response.get('id')

        return topic_id

    topic_programming = create_dummy_topic('programming', 'Programming', 'All about programming.', user_foo_response)
    topic_music = create_dummy_topic('music', 'Music', 'Discussion about music.', user_john_response)
    topic_sports = create_dummy_topic('sports', 'Sports', 'All about sports.', user_trump_response)
    topic_movies = create_dummy_topic('movies', 'Movies', 'Discussion about movies.', user_elon_response)
    topic_books = create_dummy_topic('books', 'Books', 'All about books.', user_james_response)
    topic_technology = create_dummy_topic('technology', 'Technology', 'Latest trends in technology.', user_elon_response)
    topic_gaming = create_dummy_topic('gaming', 'Gaming', 'Everything about games.', user_foo_response)
    topic_travel = create_dummy_topic('travel', 'Travel', 'Travel tips and experiences.', user_james_response)
    topic_food = create_dummy_topic('food', 'Food', 'Delicious recipes and restaurants.', user_bar_response)
    topic_science = create_dummy_topic('science', 'Science', 'Discuss scientific discoveries.', user_john_response)
    topic_art = create_dummy_topic('art', 'Art', 'Art and creativity discussions.', user_freddie_response)
    topic_photography = create_dummy_topic('photography', 'Photography', 'Photography tips and gear.', user_trump_response)
    topic_history = create_dummy_topic('history', 'History', 'Discussion on historical events.', user_eminem_response)
    topic_politics = create_dummy_topic('politics', 'Politics', 'Debates on political topics.', user_bar_response)
    topic_space = create_dummy_topic('space', 'Space', 'Exploring the universe.', user_elon_response)
    topic_finance = create_dummy_topic('finance', 'Finance', 'Money, stocks, and investing.', user_trump_response)
    topic_health = create_dummy_topic('health', 'Health', 'Fitness and wellness.', user_james_response)
    topic_education = create_dummy_topic('education', 'Education', 'Learning and teaching.', user_foo_response)
    topic_environment = create_dummy_topic('environment', 'Environment', 'Climate and sustainability.', user_john_response)
    topic_pets = create_dummy_topic('pets', 'Pets', 'For all pet lovers.', user_eminem_response)
    topic_cars = create_dummy_topic('cars', 'Cars', 'Automobile news and reviews.', user_elon_response)
    topic_fashion = create_dummy_topic('fashion', 'Fashion', 'Style and trends.', user_freddie_response)
    topic_photography_gear = create_dummy_topic('photographygear', 'Photography Gear', 'Camera equipment discussions.', user_trump_response)
    topic_coding_tips = create_dummy_topic('codingtips', 'Coding Tips', 'Share your coding tricks.', user_foo_response)
    topic_startup = create_dummy_topic('startup', 'Startup', 'Entrepreneurship and startups.', user_elon_response)

    # dummy posts
    def create_dummy_post(title, content, topicSlug, user):
        post_data = {
            'title': title,
            'content': content,
            'topicSlug': topicSlug
        }
        headers = {
            'Authorization': f'Bearer {user['accessToken']}'
        }
        create_post_response = api_call('posts', method='POST', data=post_data, headers=headers)
        post_id = create_post_response.get('id')

        return post_id

    post_1 = create_dummy_post('Hello World', 'This is my first post!', 'programming', user_foo_response) # postId: 1
    post_2 = create_dummy_post('What\'s your favorite programming language?', 'I really love Python!', 'programming', user_trump_response) # postId: 2
    post_3 = create_dummy_post('Let\'s write the Clean Code', 'I think we should follow the SOLID principles.', 'programming', user_elon_response) # postId: 3
    post_4 = create_dummy_post('About my Gears..', 'I love my PRS, Fender BlackOne, Dumble Amp, PedalBoard and more.. test', 'music', user_john_response) # postId: 4
    post_5 = create_dummy_post('Sports Update', 'The local team won their match!', 'sports', user_trump_response) # postId: 5
    post_6 = create_dummy_post('Movie Review', 'I just watched the latest blockbuster.', 'movies', user_elon_response) # postId: 6
    post_7 = create_dummy_post('Book Club', 'Let\'s discuss our favorite books.', 'books', user_james_response) # postId: 7
    post_8 = create_dummy_post('Rap Battle', 'Who is the best rapper of all time?', 'music', user_eminem_response) # postId: 8
    post_9 = create_dummy_post('AI is changing the world', 'Artificial Intelligence is revolutionizing industries.', 'technology', user_elon_response)  # 9
    post_10 = create_dummy_post('Best games of 2025', 'Which games are you excited about?', 'gaming', user_foo_response)  # 10
    post_11 = create_dummy_post('My trip to Iceland', 'The landscapes were breathtaking.', 'travel', user_james_response)  # 11
    post_12 = create_dummy_post('Top 10 pasta recipes', 'Sharing my favorite pasta dishes.', 'food', user_bar_response)  # 12
    post_13 = create_dummy_post('Latest Mars Rover discoveries', 'NASA released new photos.', 'space', user_elon_response)  # 13
    post_14 = create_dummy_post('Best DSLR for beginners', 'Looking for camera suggestions.', 'photography', user_trump_response)  # 14
    post_15 = create_dummy_post('Healthy morning routines', 'Start your day the right way.', 'health', user_james_response)  # 15
    post_16 = create_dummy_post('Investing in 2025', 'Where to put your money?', 'finance', user_trump_response)  # 16
    post_17 = create_dummy_post('Climate change facts', 'We need urgent action.', 'environment', user_john_response)  # 17
    post_18 = create_dummy_post('Caring for your dog', 'Tips for keeping pets healthy.', 'pets', user_eminem_response)  # 18
    post_19 = create_dummy_post('Electric cars in 2025', 'Are EVs finally mainstream?', 'cars', user_elon_response)  # 19
    post_20 = create_dummy_post('Street fashion trends', 'What’s hot this year?', 'fashion', user_freddie_response)  # 20
    post_21 = create_dummy_post('Python tips for beginners', 'Useful shortcuts and tricks.', 'codingtips', user_foo_response)  # 21
    post_22 = create_dummy_post('Launching my startup', 'Lessons learned in the first year.', 'startup', user_elon_response)  # 22
    post_23 = create_dummy_post('TypeScript vs JavaScript', 'Pros/cons and migration tips.', 'programming', user_foo_response)  # 23
    post_24 = create_dummy_post('Building REST APIs with NestJS', 'Routing, pipes, guards quickstart.', 'programming', user_john_response)  # 24
    post_25 = create_dummy_post('Best Coding Keyboards in 2025', 'Low-profile vs tactile, QMK/VIA.', 'technology', user_elon_response)  # 25
    post_26 = create_dummy_post('Unreal Engine 6 Highlights', 'Lumen 2.0 and Nanite updates.', 'gaming', user_trump_response)  # 26
    post_27 = create_dummy_post('Seoul Food Tour Guide', 'Hidden gems in Ikseon-dong.', 'travel', user_james_response)  # 27
    post_28 = create_dummy_post('Fermentation Basics', 'Kimchi, kombucha, sourdough at home.', 'food', user_bar_response)  # 28
    post_29 = create_dummy_post('Black Hole Imaging Update', 'Interferometry breakthroughs explained.', 'science', user_john_response)  # 29
    post_30 = create_dummy_post('Watercolor Tips for Beginners', 'Brush control and paper selection.', 'art', user_freddie_response)  # 30
    post_31 = create_dummy_post('Prime vs Zoom Lenses', 'When to choose which and why.', 'photography', user_trump_response)  # 31
    post_32 = create_dummy_post('WWII Maps Worth Studying', 'Operational vs strategic maps.', 'history', user_eminem_response)  # 32
    post_33 = create_dummy_post('Polling Models 101', 'Bayesian vs frequentist approaches.', 'politics', user_bar_response)  # 33
    post_34 = create_dummy_post('Starship Progress Tracker', 'Flight test notes and timelines.', 'space', user_elon_response)  # 34
    post_35 = create_dummy_post('ETF or Individual Stocks?', 'Risk, fees, and tax lots.', 'finance', user_trump_response)  # 35
    post_36 = create_dummy_post('Zone 2 Training Guide', 'Heart rate, mitochondria, sample week.', 'health', user_james_response)  # 36
    post_37 = create_dummy_post('Learning Algorithms Roadmap', 'Greedy, DP, graphs, practice sets.', 'education', user_foo_response)  # 37
    post_38 = create_dummy_post('Zero-Waste Habits', 'Small wins that compound.', 'environment', user_john_response)  # 38
    post_39 = create_dummy_post('Cat Nutrition 101', 'Wet vs dry, taurine myths.', 'pets', user_eminem_response)  # 39
    post_40 = create_dummy_post('Best Home EV Chargers', '11kW vs 7kW, cable management.', 'cars', user_elon_response)  # 40
    post_41 = create_dummy_post('Capsule Wardrobe Guide', 'Silhouette, palette, fabric.', 'fashion', user_freddie_response)  # 41
    post_42 = create_dummy_post('Budget Camera Kits 2025', 'Bodies + primes under $1k.', 'photographygear', user_trump_response)  # 42
    post_43 = create_dummy_post('Must-Have VSCode Extensions', 'Lint, test, Git superpowers.', 'codingtips', user_foo_response)  # 43
    post_44 = create_dummy_post('Bootstrapping Stories', 'What I learned spending $0 on ads.', 'startup', user_elon_response)  # 44
    post_45 = create_dummy_post('Top 10 Iconic Riffs', 'From “Gravity” to classics.', 'music', user_john_response)  # 45
    post_46 = create_dummy_post('Marathon Training (Sub 4h)', 'Base → tempo → taper plan.', 'health', user_james_response)  # 46
    post_47 = create_dummy_post('K-Drama Recommendations', 'Hidden gems beyond blockbusters.', 'movies', user_foo_response)  # 47
    post_48 = create_dummy_post('Underrated Sci-Fi Books', 'Beyond Asimov & Clarke.', 'books', user_john_response)  # 48
    post_49 = create_dummy_post('GraphQL vs REST', 'Trade-offs, caching, schema drift.', 'programming', user_elon_response)  # 49
    post_50 = create_dummy_post('Rust Borrow Checker Tricks', 'Lifetimes, ownership patterns.', 'programming', user_trump_response)  # 50
    post_51 = create_dummy_post('Home Lab Builds 2025', 'Proxmox, ZFS, low-power nodes.', 'technology', user_foo_response)  # 51
    post_52 = create_dummy_post('Pet Photo Thread 📸', 'Share your cutest pet moments!', 'pets', user_freddie_response)  # 52

    def create_dummy_comment(content, postId, user):
        comment_data = {
            'content': content
        }
        headers = {
            'Authorization': f'Bearer {user['accessToken']}'
        }
        return api_call(f'posts/{postId}/comments', method='POST', data=comment_data, headers=headers)

    def bulk_comments(post_id, items):
        for content, u in items:
            create_dummy_comment(content, post_id, u)

    create_dummy_comment('Great post!', post_1, user_foo_response)
    create_dummy_comment('I totally agree with you.', post_2, user_trump_response)
    create_dummy_comment('This is very insightful.', post_3, user_elon_response)
    create_dummy_comment('Thanks for sharing!', post_4, user_james_response)
    create_dummy_comment('I have a different opinion.', post_5, user_eminem_response)
    create_dummy_comment('AI is fascinating!', post_9, user_john_response)
    create_dummy_comment('I loved The Witcher 4!', post_10, user_trump_response)
    create_dummy_comment('Iceland is on my bucket list.', post_11, user_freddie_response)
    create_dummy_comment('Yummy!', post_12, user_eminem_response)
    create_dummy_comment('Mars looks amazing!', post_13, user_foo_response)
    create_dummy_comment('I recommend the Canon EOS 90D.', post_14, user_james_response)
    create_dummy_comment('Routine is everything.', post_15, user_bar_response)
    create_dummy_comment('I’m investing in renewable energy.', post_16, user_elon_response)
    create_dummy_comment('Agreed, we need change now.', post_17, user_trump_response)
    create_dummy_comment('Dogs are the best!', post_18, user_john_response)
    create_dummy_comment('Tesla Model 3 is great.', post_19, user_foo_response)
    create_dummy_comment('Love the oversized look.', post_20, user_freddie_response)
    create_dummy_comment('Thanks for the Python tips!', post_21, user_james_response)
    create_dummy_comment('Good luck with your startup.', post_22, user_bar_response)

    # dummy post likes
    def create_likes(postId, user):
        headers = {
            'Authorization': f'Bearer {user['accessToken']}'
        }
        return api_call(f'likes/{postId}', method='POST', headers=headers)
    
    def bulk_likes(post_id, users):
        for u in users:
            create_likes(post_id, u)

    create_likes(post_1, user_foo_response)
    create_likes(post_1, user_trump_response)
    create_likes(post_1, user_elon_response)
    create_likes(post_5, user_eminem_response)
    create_likes(post_2, user_trump_response)
    create_likes(post_2, user_bar_response)
    create_likes(post_3, user_elon_response)
    create_likes(post_4, user_james_response)
    create_likes(post_5, user_foo_response)
    create_likes(post_9, user_foo_response)
    create_likes(post_9, user_john_response)
    create_likes(post_10, user_trump_response)
    create_likes(post_10, user_elon_response)
    create_likes(post_11, user_freddie_response)
    create_likes(post_12, user_eminem_response)
    create_likes(post_13, user_foo_response)
    create_likes(post_13, user_james_response)
    create_likes(post_14, user_bar_response)
    create_likes(post_15, user_trump_response)
    create_likes(post_16, user_elon_response)
    create_likes(post_17, user_john_response)
    create_likes(post_18, user_eminem_response)
    create_likes(post_19, user_foo_response)
    create_likes(post_20, user_freddie_response)
    create_likes(post_21, user_james_response)
    create_likes(post_22, user_elon_response)

    # 23 ~
    bulk_comments(23, [
        ('TS types saved my project.', user_john_response),
        ('Enums vs union types—what do you prefer?', user_trump_response),
        ('Use ts-node-dev in dev, esbuild in prod.', user_elon_response),
    ])
    bulk_likes(23, [user_foo_response, user_john_response, user_elon_response, user_james_response])

    # 24
    bulk_comments(24, [
        ('Guards + interceptors = 🔥', user_foo_response),
        ('Swagger setup tips?', user_james_response),
    ])
    bulk_likes(24, [user_john_response, user_foo_response, user_bar_response])

    # 25
    bulk_comments(25, [
        ('Low-profile is great for wrists.', user_bar_response),
        ('QMK layers changed my life.', user_eminem_response),
        ('I still love buckling springs.', user_freddie_response),
    ])
    bulk_likes(25, [user_elon_response, user_trump_response, user_foo_response, user_freddie_response])

    # 26
    bulk_comments(26, [
        ('Lumen 2.0 in UE6 is wild.', user_elon_response),
        ('How’s editor stability?', user_foo_response),
    ])
    bulk_likes(26, [user_trump_response, user_john_response, user_foo_response])

    # 27
    bulk_comments(27, [
        ('Ikseon-dong dessert spots pls!', user_freddie_response),
        ('Try cold noodles near Anguk.', user_john_response),
        ('Map please?', user_bar_response),
    ])
    bulk_likes(27, [user_james_response, user_john_response, user_freddie_response, user_bar_response])

    # 28
    bulk_comments(28, [
        ('Sourdough starter name ideas?', user_eminem_response),
        ('Use 2% salt for kimchi base.', user_foo_response),
    ])
    bulk_likes(28, [user_bar_response, user_foo_response, user_james_response])

    # 29
    bulk_comments(29, [
        ('Link to the paper?', user_elon_response),
        ('Great explainer on baselines.', user_james_response),
    ])
    bulk_likes(29, [user_john_response, user_elon_response, user_trump_response])

    # 30
    bulk_comments(30, [
        ('Cold-press paper changed everything.', user_freddie_response),
        ('Round vs flat wash brush?', user_john_response),
    ])
    bulk_likes(30, [user_freddie_response, user_john_response])

    # 31
    bulk_comments(31, [
        ('Primes for low light any day.', user_james_response),
        ('Zooms on travel = convenience.', user_foo_response),
        ('Sigma 18-35 still king.', user_eminem_response),
    ])
    bulk_likes(31, [user_trump_response, user_foo_response, user_james_response, user_eminem_response])

    # 32
    bulk_comments(32, [
        ('Love operational art analyses.', user_bar_response),
        ('Recommended atlases?', user_john_response),
    ])
    bulk_likes(32, [user_eminem_response, user_john_response, user_bar_response])

    # 33
    bulk_comments(33, [
        ('Model calibration matters most.', user_elon_response),
        ('Weighting by recency is tricky.', user_trump_response),
    ])
    bulk_likes(33, [user_bar_response, user_elon_response, user_trump_response])

    # 34
    bulk_comments(34, [
        ('Heat shield tiles update?', user_foo_response),
        ('Stage-0 spin stabilization?', user_james_response),
        ('Flight cadence guesses?', user_john_response),
    ])
    bulk_likes(34, [user_elon_response, user_foo_response, user_john_response, user_james_response])

    # 35
    bulk_comments(35, [
        ('ETFs for lazy portfolios.', user_john_response),
        ('Direct indexing if tax savvy.', user_elon_response),
    ])
    bulk_likes(35, [user_trump_response, user_john_response, user_elon_response])

    # 36
    bulk_comments(36, [
        ('Zone 2 + sleep = gains.', user_foo_response),
        ('Polarized training works.', user_freddie_response),
        ('How to test LT1?', user_bar_response),
    ])
    bulk_likes(36, [user_james_response, user_foo_response, user_freddie_response, user_bar_response])

    # 37
    bulk_comments(37, [
        ('DP → graphs → matroid fun.', user_elon_response),
        ('Practice on AtCoder & CF.', user_trump_response),
    ])
    bulk_likes(37, [user_foo_response, user_elon_response, user_trump_response])

    # 38
    bulk_comments(38, [
        ('Refill stations are underrated.', user_john_response),
        ('Repair > replace mindset.', user_james_response),
    ])
    bulk_likes(38, [user_john_response, user_james_response, user_foo_response])

    # 39
    bulk_comments(39, [
        ('Wet food fixed hairballs for us.', user_bar_response),
        ('Vet said watch phosphorus.', user_john_response),
    ])
    bulk_likes(39, [user_eminem_response, user_bar_response, user_john_response, user_foo_response, user_james_response])

    # 40
    bulk_comments(40, [
        ('Load balancing tips?', user_foo_response),
        ('Cable length matters in winter!', user_trump_response),
    ])
    bulk_likes(40, [user_elon_response, user_trump_response, user_foo_response])

    # 41
    bulk_comments(41, [
        ('Merino tees are clutch.', user_james_response),
        ('Tailor your pants hem!', user_freddie_response),
    ])
    bulk_likes(41, [user_freddie_response, user_james_response, user_john_response])

    # 42
    bulk_comments(42, [
        ('Used X-T30 + 35/2 is perfect.', user_trump_response),
        ('Don’t forget extra batteries.', user_foo_response),
    ])
    bulk_likes(42, [user_trump_response, user_foo_response, user_eminem_response, user_bar_response, user_john_response])

    # 43
    bulk_comments(43, [
        ('GitLens + Error Lens combo.', user_john_response),
        ('Thunder Client beats Postman for me.', user_foo_response),
    ])
    bulk_likes(43, [user_foo_response, user_john_response, user_elon_response])

    # 44
    bulk_comments(44, [
        ('Founder-market fit matters.', user_bar_response),
        ('Ship fast, talk to users.', user_elon_response),
        ('Congrats on MRR!', user_james_response),
    ])
    bulk_likes(44, [user_elon_response, user_bar_response, user_james_response, user_foo_response])

    # 45
    bulk_comments(45, [
        ('That PRS tone though…', user_foo_response),
        ('Add some Hendrix too!', user_eminem_response),
    ])
    bulk_likes(45, [user_john_response, user_foo_response, user_eminem_response, user_freddie_response])

    # 46
    bulk_comments(46, [
        ('Negative splits worked for me.', user_john_response),
        ('Fuel every 30–40 mins.', user_elon_response),
    ])
    bulk_likes(46, [user_james_response, user_john_response, user_elon_response])

    # 47
    bulk_comments(47, [
        ('Slice-of-life picks please.', user_james_response),
        ('OSTs are so good lately.', user_freddie_response),
    ])
    bulk_likes(47, [user_foo_response, user_freddie_response, user_james_response, user_elon_response, user_bar_response, user_eminem_response])

    # 48
    bulk_comments(48, [
        ('Try “Blindsight”.', user_trump_response),
        ('Also “The Three-Body Problem”.', user_elon_response),
    ])
    bulk_likes(48, [user_john_response, user_elon_response, user_trump_response])

    # 49
    bulk_comments(49, [
        ('GraphQL caching is hard.', user_foo_response),
        ('REST shines for CDN caching.', user_james_response),
        ('Schema stitching war stories?', user_john_response),
    ])
    bulk_likes(49, [user_elon_response, user_foo_response, user_james_response, user_john_response])

    # 50
    bulk_comments(50, [
        ('Use Cow<' 'a> patterns carefully.', user_foo_response),
        ('Borrow checker is a teacher.', user_john_response),
    ])
    bulk_likes(50, [user_trump_response, user_foo_response, user_john_response])

    # 51
    bulk_comments(51, [
        ('ZFS snapshots saved me.', user_bar_response),
        ('iGPU Quick Sync for Plex!', user_elon_response),
    ])
    bulk_likes(51, [user_foo_response, user_bar_response, user_elon_response])

    # 52
    bulk_comments(52, [
        ('My cat owns this thread.', user_eminem_response),
        ('Golden retriever here! 🐶', user_james_response),
        ('I’ll shoot with a nifty fifty.', user_trump_response),
    ])
    bulk_likes(52, [user_freddie_response, user_eminem_response, user_james_response, user_trump_response])


    # 개추 주작은 뭐야
    create_dummy_post('개추 주작은 뭐야', '개추 주작은 뭐야', 'programming', user_foo_response)  # postId: 53
    bulk_comments(53, [
        ('개추', user_foo_response),
        ('개추', user_elon_response)
    ])
    bulk_likes(53, [user_foo_response, user_elon_response, user_bar_response, user_john_response, user_eminem_response, user_freddie_response, user_james_response, user_trump_response])

    # Follow

    def create_follow(user, target_user):
        headers = {
            'Authorization': f'Bearer {user["accessToken"]}',
            'Content-Type': 'application/json'
        }
        return api_call(f'subscription/follow/{target_user["username"]}', method='POST', headers=headers)

    create_follow(user_foo_response, user_john_response)
    create_follow(user_foo_response, user_james_response)
    create_follow(user_foo_response, user_elon_response)
    create_follow(user_foo_response, user_bar_response)
    create_follow(user_foo_response, user_eminem_response)
    create_follow(user_foo_response, user_freddie_response)

    create_follow(user_john_response, user_foo_response)
    create_follow(user_james_response, user_foo_response)
    create_follow(user_elon_response, user_foo_response)
    create_follow(user_bar_response, user_foo_response)
    create_follow(user_eminem_response, user_foo_response)
    create_follow(user_freddie_response, user_foo_response)
    create_follow(user_trump_response, user_foo_response)
    create_follow(user_james_response, user_john_response)
    create_follow(user_elon_response, user_john_response)
    create_follow(user_bar_response, user_john_response)
    create_follow(user_eminem_response, user_john_response)
    create_follow(user_freddie_response, user_john_response)

    create_follow(user_james_response, user_elon_response)
    create_follow(user_bar_response, user_elon_response)
    create_follow(user_eminem_response, user_elon_response)
    create_follow(user_freddie_response, user_elon_response)

    create_follow(user_freddie_response, user_bar_response)
    create_follow(user_trump_response, user_bar_response)
    create_follow(user_james_response, user_bar_response)
