import React, { useState } from "react";
import AMONGUS from "./assets/measf.png";

function LoggedOut({ onNavigate }) {
  const [isPopupVisible, setPopupVisible] = useState(false);
  const [inputs, setInputs] = useState({
    input1: "",
    input2: "",
    input3: "",
    input4: "",
    input5: "",
  });

  const openPopup = () => {
    setPopupVisible(true);
  };

  const closePopup = () => {
    setPopupVisible(false);
  };

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setInputs((prev) => ({
      ...prev,
      [name]: value,
    }));
  };

  const submitForm = () => {
    console.log(inputs);
    closePopup();
  };

  return (
    <div className="andrew-fullpage">
      {isPopupVisible && (
        <div className="andrew-popupfullpage">
          <div className="andrew-popupcontainer">
            <div>
              <div className="andrew-popuptop">
                <div> </div>
                <div className="andrew-popuptoptitle">Information Editor</div>
                <div className="x" onClick={closePopup}>
                  &times;
                </div>
              </div>
              <form className="andrew-popupcontent">
                Variable 1
                <input
                  type="text"
                  placeholder="..."
                  name="input1"
                  value={inputs.input1}
                  onChange={handleInputChange}
                />
                Variable 2
                <input
                  type="text"
                  placeholder="..."
                  name="input2"
                  value={inputs.input2}
                  onChange={handleInputChange}
                />
                Variable 3
                <input
                  type="text"
                  placeholder="..."
                  name="input3"
                  value={inputs.input3}
                  onChange={handleInputChange}
                />
                Variable 4
                <input
                  type="text"
                  placeholder="..."
                  name="input4"
                  value={inputs.input4}
                  onChange={handleInputChange}
                />
                Variable 5
                <select
                  name="input5"
                  className="andrew-dropdownselect"
                  value={inputs.input5}
                  onChange={handleInputChange}
                >
                  <option value="option1">MODEL 1</option>
                  <option value="option2">MODEL 2</option>
                  <option value="option3">MODEL 3</option>
                </select>
              </form>
            </div>
            <div className="andrew-popupbottom">
              <button
                type="button"
                className="andrew-popupbutton"
                onClick={submitForm}
              >
                Confirm
              </button>
            </div>
          </div>
        </div>
      )}
      <div className="andrew-tophalf">
        <div className="andrew-lefthalf">
          <div className="andrew-graphcontainer">
            <div className="andrew-graphtitle">Chart 1</div>
            <img className="andrew-graph" src={AMONGUS} />
          </div>
        </div>
        <div className="andrew-righthalf">
          <div className="andrew-graphcontainer">
            <div className="andrew-graphtitle">Chart 2</div>
            <img className="andrew-graph" src={AMONGUS} />
          </div>
        </div>
      </div>
      <div className="andrew-bottomhalf">
        <div className="andrew-lefthalf">
          <div className="andrew-graphcontainer">
            <div className="andrew-graphtitle">Chart 3</div>
            <img className="andrew-graph" src={AMONGUS} />
          </div>
        </div>
        <div className="andrew-righthalf">
          <div className="andrew-textinfocontainer">
            <div className="andrew-textinfo">TEXT INFO</div>
            <button className="andrew-textinfobutton" onClick={openPopup}>
              Open Editor
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}

export default LoggedOut;