import scipy.interpolate as scp_int
import numpy as np


def interp_Phi_dqh(self, Id, Iq):
    """Get the magnets d-axis inductance
    Parameters
    ----------
    self : LUTdq
        a LUTdq object
    Id : float
        current Id
    Iq : float
        current Iq

    Returns
    ----------
    Phi_dqh : ndarray
        interpolated flux in dqh frame (3)
    """

    # Compute interpolant at first call
    if self.Phi_dqh_interp is None:
        # Get unique Id, Iq, assuming regular grid
        XId, XIq = np.unique(self.OP_matrix[:, 1]), np.unique(self.OP_matrix[:, 2])
        # Sort in ascending order
        self.Phi_dqh_interp = scp_int.RegularGridInterpolator(
            (XId, XIq),
            self.get_Phidqh_mean()[:, 0:2].reshape((len(XId), len(XIq), 2)),
            method="linear",
        )

    # Perform 2D interpolation
    return self.Phi_dqh_interp((Id, Iq))