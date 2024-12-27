import { Button, Stack, Table, TableBody, TableCell, TableContainer, TableHead, TableRow, TextField } from "@mui/material"
import axios from "axios"
import { useEffect, useRef, useState } from "react"
import { UserModel } from "../models/UserModel"
import { GetUsersModel } from "../models/GetUsersModel"
import { DeleteUserModel } from "../models/DeleteUserMode"
import { DataGrid, GridColDef } from '@mui/x-data-grid';
import { GetPostModel } from "../models/GetPostModel"
import { DeletePostModel } from "../models/DeletePostModel"


function GetPage(){

    const columns_user = [
        { field: 'id', headerName: 'ID', width: 100, editable: false },
        { field: 'username', headerName: 'username', width: 200, editable: true},
        { field: 'email', headerName: 'email', width: 200, editable: true },
        { field: 'password', headerName: 'password', width: 200, editable: true },
        { field: 'delete', headerName: 'delete', width: 200,
            renderCell: (params: any) => <Button variant="contained" onClick={() => {
                DeleteUserHandle(params.row.id)
                setDeleteUserButton(!deleteUserButton)
            }}>Удалить</Button>
        }
    ];

    const columns_post = [
        { field: 'id', headerName: 'ID', width: 100, editable: false },
        { field: 'title', headerName: 'title', width: 200, editable: true},
        { field: 'content', headerName: 'content', width: 200, editable: true },
        { field: 'user_id', headerName: 'user_id', width: 200, editable: true },
        { field: 'delete', headerName: 'delete', width: 200,
            renderCell: (params: any) => <Button variant="contained" onClick={() => {
                DeletePostHandle(params.row.id)
                setDeletePostButton(!deletePostButton)
            }}>Удалить</Button>
        }
    ];

    const[deleteUserButton, setDeleteUserButton] = useState<boolean>(false)
    const[deletePostButton, setDeletePostButton] = useState<boolean>(false)
    const[initUsersData, setInitUsersData] = useState<GetUsersModel[]>()
    const[initPostData, setInitPostData] = useState<GetPostModel[]>()

    const updateUser = (user: GetUsersModel) => {
        axios.put("http://127.0.0.1:8000/api/user/update", user, {})
        .then((response) => console.log(response))
    }

    const updatePost = (post: GetPostModel) => {
        axios.put("http://127.0.0.1:8000/api/post/update", post, {})
        .then((response) => console.log(response))
    }

    useEffect(() => {
        axios.get("http://127.0.0.1:8000/api/users")
        .then((response) => {
            setInitUsersData(response.data)
        })

        axios.get("http://127.0.0.1:8000/api/posts")
        .then((response) => setInitPostData(response.data))
    }, [])

    useEffect(() => {
        axios.get("http://127.0.0.1:8000/api/users")
        .then((response) => {
            setInitUsersData(response.data)
        })
    }, [deleteUserButton])

    useEffect(() => {
        axios.get("http://127.0.0.1:8000/api/posts")
        .then((response) => {
            setInitPostData(response.data)
        })
    }, [deletePostButton])

    const DeleteUserHandle = (idUser: number) => {
        let deleteUser: DeleteUserModel = {id: idUser} 
        axios.delete("http://127.0.0.1:8000/api/user/delete", {data: deleteUser})
        .then(() => console.log("Пользователь удален"))
    }

    const DeletePostHandle = (idPost: number) => {
        let deletePost: DeletePostModel = {id: idPost} 
        axios.delete("http://127.0.0.1:8000/api/post/delete", {data: deletePost})
        .then(() => console.log("Пост удален"))
    }

    return(
        <Stack spacing={2}>
            <DataGrid key="table_user" columns={columns_user} rows={initUsersData} editMode="cell"
                onCellEditStart={(e) => updateUser(e.row)}
            />
            <DataGrid key="table_post" columns={columns_post} rows={initPostData} editMode="cell"
                onCellEditStart={(e) => updatePost(e.row)}
            />
        </Stack>
    )
}

export default GetPage