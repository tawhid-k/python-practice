def replace_domain(email, new, old=None):
    newemail = email[:str(email).find('@')+1] + new
    return newemail
    
print(replace_domain('alice@kaaj.com','sheba.xyz','kaaj.com'))
print(replace_domain('bob@sheba.xyz', 'sheba.xyz'))