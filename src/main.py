import json
import requests

def returnGithubInfos(user, option):
    if(option == 1):
        if(not user):
            print('Porfavor insira um usário')

        else:
            githubUserContent = requests.get(f'https://api.github.com/users/{user}').json()

            serializedUser = {
                'name': githubUserContent['name'],
                'followers': githubUserContent['followers'],
                'following': githubUserContent['following'],
                'reposQuantitiy': githubUserContent['public_repos']
                }
                
            if(not githubUserContent['name']):
                print('Porfavor insira um usuário valido')
                
            else:
                with open(f"./savedUsers/{githubUserContent['node_id']}.json", 'w') as outfile:
                    json.dump(serializedUser, outfile)

                print(f'Usuário salvo com sucesso, informações: \n {serializedUser} \n \n \n \n \n')

    elif(option == 2):
        if(not user):
            print('Porfavor insira um usário')

        else:
            githubUserContent = requests.get(f'https://api.github.com/users/{user}').json()
            
            serializedUser = {
                'name': githubUserContent['name'],
                'followers': githubUserContent['followers'],
                'following': githubUserContent['following'],
                'reposQuantitiy': githubUserContent['public_repos']
                }


            if(not githubUserContent['name']):
                print('Porfavor insira um usuário valido')
            else:
                print(f'Usuário não foi salvo, informações:\n {serializedUser} \n \n \n \n \n')    
        
            
    else:
        print('Selecione uma das opções validas')

returnGithubInfos(input('Porfavor insira o nome do usuário que deseja ver as informações: '), int(input('\n [1] Salvar e ver informações \n [2] Apenas ver as informações \n \n')))
