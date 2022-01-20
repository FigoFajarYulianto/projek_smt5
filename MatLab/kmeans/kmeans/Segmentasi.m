              function varargout = Segmentasi(varargin)
% SEGMENTASI MATLAB code for Segmentasi.fig
%      SEGMENTASI, by itself, creates a new SEGMENTASI or raises the existing
%      singleton*.
%
%      H = SEGMENTASI returns the handle to a new SEGMENTASI or the handle to
%      the existing singleton*.
%
%      SEGMENTASI('CALLBACK',hObject,eventData,handles,...) calls the local
%      function named CALLBACK in SEGMENTASI.M with the given input arguments.
%
%      SEGMENTASI('Property','Value',...) creates a new SEGMENTASI or raises the
%      existing singleton*.  Starting from the left, property value pairs are
%      applied to the GUI before Segmentasi_OpeningFcn gets called.  An
%      unrecognized property name or invalid value makes property application
%      stop.  All inputs are passed to Segmentasi_OpeningFcn via varargin.
%
%      *See GUI Options on GUIDE's Tools menu.  Choose "GUI allows only one
%      instance to run (singleton)".
%
% See also: GUIDE, GUIDATA, GUIHANDLES

% Edit the above text to modify the response to help Segmentasi

% Last Modified by GUIDE v2.5 04-Dec-2021 13:33:44

% Begin initialization code - DO NOT EDIT
gui_Singleton = 1;
gui_State = struct('gui_Name',       mfilename, ...
                   'gui_Singleton',  gui_Singleton, ...
                   'gui_OpeningFcn', @Segmentasi_OpeningFcn, ...
                   'gui_OutputFcn',  @Segmentasi_OutputFcn, ...
                   'gui_LayoutFcn',  [] , ...
                   'gui_Callback',   []);
if nargin && ischar(varargin{1})
    gui_State.gui_Callback = str2func(varargin{1});
end

if nargout
    [varargout{1:nargout}] = gui_mainfcn(gui_State, varargin{:});
else
    gui_mainfcn(gui_State, varargin{:});
end
% End initialization code - DO NOT EDIT

% --- Executes just before Segmentasi is made visible.
function Segmentasi_OpeningFcn(hObject, eventdata, handles, varargin)
% This function has no output args, see OutputFcn.
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
% varargin   command line arguments to Segmentasi (see VARARGIN)

% Choose default command line output for Segmentasi
handles.output = hObject;

% Update handles structure
guidata(hObject, handles);

% UIWAIT makes Segmentasi wait for user response (see UIRESUME)
% uiwait(handles.figure1);


% --- Outputs from this function are returned to the command line.
function varargout = Segmentasi_OutputFcn(hObject, eventdata, handles) 
% varargout  cell array for returning output args (see VARARGOUT);
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Get default command line output from handles structure
varargout{1} = handles.output;

% --- Executes on button press in buttonInput.
function buttonInput_Callback(hObject, eventdata, handles)
% hObject    handle to buttonInput (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

[nama_file,nama_path] = uigetfile({'*.jpg';'*.jpeg';'*.png';'*.HEIC';});
if ~isequal(nama_file,0)
    handles.data1 = imread(fullfile(nama_path,nama_file));
    guidata(hObject,handles);
    axes(handles.axes1);
    imshow(handles.data1);
     complete = strcat(nama_file);
   set(handles.edit3,'string',complete);
    I = imread(complete);
else
    return
end

%handles.data1 = hObject;
%[fn, pn] = uigetfile('*.*','select jpg file');
%complete = strcat(pn, fn);
%set(handles.edit3,'string',complete);
%I = imread(complete);
%axes(handles.axes1)
%imshow(I,[]);
%guidata(hObject, handles);

% --- Executes on button press in buttonKmeans.
function buttonKmeans_Callback(hObject, eventdata, handles)
% hObject    handle to buttonKmeans (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
axes(handles.axes2);
gambar = (handles.data1);
gambar = im2double(gambar); %agar tidak terjadi error
r = gambar(:,:,1); %kita ambil warnanya
g = gambar(:,:,2);
b = gambar(:,:,3);
[m,n] = size(r); %mengambil ukuran gambar
r = reshape(r,m*n,1); %menjadikan warna dan ukuran gambar menjadi data
g = reshape(g,m*n,1);
b = reshape(b,m*n,1);
rgb = cat(2,r,g,b);
h = kmeans(rgb,3); %angka 3 ini adalah jumlah cluster
h = reshape(h,m,n);
h = h/3;
imshow(h);

% --- Executes on button press in buttonReset.
function buttonReset_Callback(hObject, eventdata, handles)
% hObject    handle to buttonReset (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
axes(handles.axes2);
gambar = (handles.data1);
imshow(gambar);


% --- Executes on button press in pushbutton9.
function pushbutton9_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton9 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
gray = handles.data5;
value = graythresh(gray);
thresh = im2bw(gray,value);
thresh = imcomplement(thresh);
axes(handles.axes11);
imshow(thresh);
handles.data6 = thresh;
guidata(hObject,handles);
set(handles.edit2,'String',value)

function edit2_Callback(hObject, eventdata, handles)
% hObject    handle to edit2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of edit2 as text
%        str2double(get(hObject,'String')) returns contents of edit2 as a double


% --- Executes during object creation, after setting all properties.
function edit2_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes on button press in pushbutton10.
function pushbutton10_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton10 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
[nama_file,nama_path] = uigetfile({'*.jpg';'*.jpeg';'*.png';'*.HEIC';});
if ~isequal(nama_file,0)
    handles.data4 = imread(fullfile(nama_path,nama_file));
    guidata(hObject,handles);
    axes(handles.axes10);
    imshow(handles.data4);
else
    return
end

% --- Executes on button press in pushbutton11.
function pushbutton11_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton11 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
image1 = handles.data4;
gray = rgb2gray(image1);
axes(handles.axes11);
imshow(gray);
handles.data5 = gray;
guidata(hObject,handles);

% --- Executes on button press in pushbutton12.
function pushbutton12_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton12 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)


% --- Executes on button press in pushbutton13.
function pushbutton13_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton13 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
axes(handles.axes11);
gambar = (handles.data4);
imshow(gambar);


% --- Executes on button press in pushbutton14.
function pushbutton14_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton14 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
close


% --- Executes on button press in pushbutton16.
function pushbutton16_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton16 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

thresh = handles.data6;
[name_file_save,path_save] = uiputfile( ...
 {'*.bmp','File Bitmap (*.bmp)';...
 '*.jpg','File jpeg (*.jpg)';
 '*.tif','File Tif (*.tif)';
 '*.*','All Files (*.*)'},...
 'Save Image');
if ~isequal(name_file_save,0)
 imwrite(thresh,fullfile(path_save,name_file_save));
else
 return
end
% --- Executes on button press in pushbutton15.
function pushbutton15_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton15 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
thresh = handles.data1;
[name_file_save,path_save] = uiputfile( ...
 {'*.bmp','File Bitmap (*.bmp)';...
 '*.jpg','File jpeg (*.jpg)';
 '*.tif','File Tif (*.tif)';
 '*.*','All Files (*.*)'},...
 'Save Image');
if ~isequal(name_file_save,0)
 imwrite(thresh,fullfile(path_save,name_file_save));
else
 return
end


% --- Executes on button press in pushbutton17.
function pushbutton17_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton17 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)



function edit3_Callback(hObject, eventdata, handles)
% hObject    handle to edit3 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of edit3 as text
%        str2double(get(hObject,'String')) returns contents of edit3 as a double


% --- Executes during object creation, after setting all properties.
function edit3_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit3 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end
