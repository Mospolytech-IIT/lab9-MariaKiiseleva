import { useEffect, useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import TextField from '@mui/material/TextField'
import { Button, Stack, Typography } from '@mui/material'
import { UserModel } from '../models/UserModel'
import axios from 'axios'
import { PostModel } from '../models/PostModel'

function CreatePage(){

    const[usernameState, setUsernameState] = useState<string>("")
    const[emailState, setEmailState] = useState<string>("")
    const[passwordState, setPasswordState] = useState<string>("")

    const[createUserButton, setCreateUserButton] = useState<boolean>(false)


    const[titleState, setTitleState] = useState<string>("")
    const[contentState, setContentState] = useState<string>("")
    const[userIdState, setUserIdState] = useState<string>("")

    const[createPostButton, setCreatePostButton] = useState<boolean>(false)



    useEffect(() => {
        let newUser : UserModel = {username: usernameState, email: emailState, password: passwordState}
        if(newUser.email != "" && newUser.username != "" && newUser.password != ""){
            axios.post("http://127.0.0.1:8000/api/user/add", newUser, {}).then((response) => console.log(response))
        }
        else{
            console.log("Wrong data")
        }
    }, [createUserButton])

    useEffect(() => {
        if(titleState != "" && contentState != "" && userIdState != "" && Number.isInteger(parseInt(userIdState, 10))){
            let newPost: PostModel = {title: titleState, content: contentState, user_id: parseInt(userIdState, 10)}
            axios.post("http://127.0.0.1:8000/api/post/add", newPost, {}).then((response) => console.log(response))
        }
        else{
            console.log("Wrong data")
        }
    }, [createPostButton])

    return(
        <Stack spacing={3}>
            <Typography variant="h3">
                кринж эээ
            </Typography>
            <Stack spacing={2}>
                <Typography>
                    Создание пользователя
                </Typography>
                <TextField id="outlined-basic" label="username" variant="outlined" onChange={(e) => setUsernameState(e.target.value)}/>
                <TextField id="outlined-basic" label="email" variant="outlined" onChange={(e) => setEmailState(e.target.value)}/>
                <TextField id="outlined-basic" label="password" variant="outlined" onChange={(e) => setPasswordState(e.target.value)}/>
                <Button variant="contained" onClick={() => setCreateUserButton(!createUserButton)}>
                    Создать
                </Button>
            </Stack>
            <Stack spacing={2}>
                <Typography>
                    Создание поста
                </Typography>
                <TextField id="outlined-basic" label="title" variant="outlined" onChange={(e) => setTitleState(e.target.value)}/>
                <TextField id="outlined-basic" label="content" variant="outlined" onChange={(e) => setContentState(e.target.value)}/>
                <TextField id="outlined-basic" label="user_id" variant="outlined" onChange={(e) => setUserIdState(e.target.value)}/>
                <Button variant="contained" onClick={() => setCreatePostButton(!createPostButton)}>
                    Создать
                </Button>
            </Stack>
        </Stack>
    )
}

export default CreatePage