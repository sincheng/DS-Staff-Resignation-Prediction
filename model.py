def save_model(df):
    # csv_file_path = filedialog.askopenfilename(filetypes=[('.csvfiles', '.csv')])
    # df = pd.read_csv(csv_file_path)
    df = df.rename(columns={ 'sales' : 'department'})
    lb = LabelEncoder()
    df['department'] = lb.fit_transform(df.department)
    df['salary'] = lb.fit_transform(df.salary)
    is_test = np.random.uniform(0, 1, len(df)) > 0.7
    train = df[is_test==False]
    test = df[is_test==True]
    x = train.drop("left",1)
    y = train.left
    cart = DecisionTreeClassifier()
    cart.fit(x,y)
    joblib.dump(cart,'cart.pkl')
    return predicted_cart
