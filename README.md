[![CircleCI](https://circleci.com/gh/WindMillCode/WindMillCodeSite.svg?style=svg)](<LINK>)


# Summary

## Features include 
Only members of the project can read the README.md from the ignore folder

# Stack 

## Frontend
* Angular v12.2.3
## Backend
* python v3.9.6
* tornado v 6.1.0

## Testing
* Docker, (tes in docker containers from linux VM) v20.10.7

### Unit
* rspec    v3.10.0
* capybara v3.35.3

### Integration
* rspec    v3.10.0
* capybara v3.35.3

### E2E
* rspec    v3.10.0
* capybara v3.35.3
* puffing billy v2.4.1

## Hosting

### CMS

### Logging

## CI/CD

## Communication
Trello


# Structure

## Linting Rules

* ruby indentation 2 lines
* ts indentation 4 lines
* we prefix all our styles with "a_p_p_" a judima methodlogy so as not to confunse with 3rd party libs
nested Loops
```js
[].forEach(x,i)=>{
    x.forEach(y,j)=>{
        y.forEach(z,k)=>{
            z.forEach(w,h)=>{
                w.forEach(xx,ii)=>{
                    ...
                })                   
            })             
        })        
    })
})
```


### Git commit messages

part 1 
[UPDATE] - any bug free updates
[PATCH]  - any partial fixes that invovles tradeoffs
[BROKEN] - any partial fixes that has issues to address
[FIX]    - meaninfgul complete fixes
[COMPLEX MERGE] - do not pull from here complex merging took place

part 2
{frontend} {backend} {CI/CD} {testing} {logging}
* where the fixes was applied 

* then the message
* can use two or more in the same commit




## Project Directory Mapping

### Frotend
#### Configurations

#### HomePage

### Backend

#### Configurations
* refer to README.md in ignore


### Testing 
* in __AngularApp/testing/TESTS.md__ we have  where we write pseudo code for our unit,e2e and integration tests later
*    __AngularApp/testing/e2e/target-e2e-circleci.rb__ - is where all of our e2e tests live, we test on docker in a ubuntu 20.04 to closely represent the circleCI env and write the code 
* in the local testing env we use a gui browser, to oberserve to  make sure the tests work properly, however in circleci we have the browsers run in headless mode. 

### CI/CD
* IN .circleci is our config.yml, we make use of the company's Docker image as well as the circleci browser-build tools orb, as a general practice we packages our dependencies into the orb so we dont have to increased build times


### Issues

### Future Plans
refer to README.md in ignore


## Site Navigation

<!-- to navigate through the website the user does what  -->
<!-- also include sub labels for each part of nav -->

### Loading of products
* handled in AngularApp\src\app\shop\main\main.component.ts



# Aspects

## Challenges

## Mistakes/Failures

## Enjoyed

## Leadership

## Conflict


## Done Different


# Issues 



# TODO

## Template Updates
Team members refer to the [Trello workspace](https://trello.com/b/AFCBbcL4/angular-template-project-updates)

## Notes


## Terminal workspace

Session 1 (Frontend)
    $(npx ng serve)
    configure frontend 
Session 2 (Backend)
    $(python tornado_server.py)
    configure backend (like heroku push)
Session 3 (Testing)
    configure testing env
    ssh session to vm to instianiate docker vm
Session 4 (Github)
    git push 
Session 5 (Logging)
    ssh session to vm to instianiate docker vm


# Resources

## Snippets
* general snippets found in planning in the trello workspace

* update user billing and shipping
```ts
    http.patch(
        `${env.backend.url}/users/update`,
        {
            data:{
                user:acctCurrent?.user,
                myPass:acctCurrent?.pass,
                update_body:myAcctCurrent
            }
        }
    )
    .pipe(
        tap(console.log,console.error)
    )
    .subscribe()
```

## Media 

[home_0.jpg]
Photo by <a href="https://unsplash.com/@markuswinkler?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Markus Winkler</a> on <a href="https://unsplash.com/s/photos/qrcode?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
  


# Metrics

## Users

## Netowrk

## Storage














