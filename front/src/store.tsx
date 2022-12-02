import thunkMiddleware from "redux-thunk";
import CombinedReducer from "./reducers/index";
import { configureStore } from "@reduxjs/toolkit";

const store = configureStore({
  reducer: CombinedReducer,
  middleware: [thunkMiddleware],
  devTools: true,
});

export default store;

export type RootState = ReturnType<typeof store.getState>;

export type AppDispatch = typeof store.dispatch;
