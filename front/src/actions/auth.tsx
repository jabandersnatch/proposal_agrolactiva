import {
  LOGIN_SUCCESS,
  LOGIN_FAIL,
  LOGOUT_SUCCESS,
  LOGOUT_FAIL,
  AUTHENTICATED_SUCCESS,
  AUTHENTICATED_FAIL,
  REFRESH_SUCCESS,
  REFRESH_FAIL,
} from "./types";

export const login =
  (username: string, password: string) => async (dispatch: any) => {
    const body = JSON.stringify({
      username,
      password,
    });
    try {
      const res = await fetch("/api/auth/login", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body,
      });
      const data = await res.json();
      if (res.status === 200) {
        dispatch({
          type: LOGIN_SUCCESS,
          payload: data,
        });
      } else {
        dispatch({
          type: LOGIN_FAIL,
        });
      }
    } catch (err) {
      dispatch({
        type: LOGIN_FAIL,
      });
    }
  };

export const logout = () => async (dispatch: any) => {
  try {
    const res = await fetch("/api/auth/logout", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
    });

    if (res.status === 200) {
      dispatch({
        type: LOGOUT_SUCCESS,
      });
    } else {
      dispatch({
        type: LOGOUT_FAIL,
      });
    }
  } catch (err) {
    dispatch({
      type: LOGOUT_FAIL,
    });
  }
};

export const check_auth_status = () => async (dispatch: any) => {
  try {
    const res = await fetch("/api/auth/refresh", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
    });
    const data = await res.json();
    if (res.status === 200) {
      dispatch({
        type: AUTHENTICATED_SUCCESS,
        payload: data,
      });
    } else {
      dispatch({
        type: AUTHENTICATED_FAIL,
      });
    }
  } catch (err) {
    dispatch({
      type: AUTHENTICATED_FAIL,
    });
  }
};

export const request_refresh = () => async (dispatch: any) => {
  try {
    const res = await fetch("/api/auth/refresh", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
    });
    if (res.status === 200) {
      dispatch({
        type: REFRESH_SUCCESS,
      });
    } else {
      dispatch({
        type: REFRESH_FAIL,
      });
    }
  } catch (err) {
    console.error(err);
  }
};
