import pandas as pd

def same_user_n_times(assignment_func, n=1000, key='color'):
    user_ids = [1] * n
    
    df = pd.DataFrame({'user_id': user_ids})
    df[key] = df['user_id'].apply(assignment_func)
    return df
    
def n_different_users(assignment_func, n=1000, key='color'):
    df = pd.DataFrame({'user_id': range(n)})
    
    df[key] = df['user_id'].apply(assignment_func)
    return df